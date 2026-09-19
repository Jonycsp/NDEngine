import math
import pytest
from engine.transforms import Rotation, apply_rotations, rotate_plane


def test_xw_rotation():
    point = [1, 0, 0, 0]
    
    result = rotate_plane(point, 0, 3, math.pi / 2)
    
    assert math.isclose(result[0], 0, abs_tol=1e-9)
    assert math.isclose(result[1], 0, abs_tol=1e-9)
    assert math.isclose(result[2], 0, abs_tol=1e-9)
    assert math.isclose(result[3], 1, abs_tol=1e-9)

def test_yw_rotation():
    point = [0, 1, 0, 0]
    
    result = rotate_plane(point, 1, 3, math.pi / 2)
    
    assert math.isclose(result[0], 0, abs_tol=1e-9)
    assert math.isclose(result[1], 0, abs_tol=1e-9)
    assert math.isclose(result[2], 0, abs_tol=1e-9)
    assert math.isclose(result[3], 1, abs_tol=1e-9)

def test_zw_rotation():
    point = [0, 0, 1, 0]
    
    result = rotate_plane(point, 2, 3, math.pi / 2)
    
    assert math.isclose(result[0], 0, abs_tol=1e-9)
    assert math.isclose(result[1], 0, abs_tol=1e-9)
    assert math.isclose(result[2], 0, abs_tol=1e-9)
    assert math.isclose(result[3], 1, abs_tol=1e-9)

def test_rotation_does_not_modify_original():
    point = [1, 2, 3, 4]
    
    rotate_plane(point, 0, 3, math.pi / 2)
    
    assert point == [1, 2, 3, 4]

def test_rotation_representation():
    rotation = Rotation(0, 3, math.pi / 2)
    
    assert rotation.i == 0
    assert rotation.j == 3
    assert math.isclose(rotation.angle, math.pi / 2)

def test_rotations_are_applied_in_order():
    point = [1, 1, 0]
    
    first_xy_then_xz = [
        Rotation(0, 1, math.pi / 2),
        Rotation(0, 2, math.pi / 2),
    ]
    
    first_xz_then_xy = [
        Rotation(0, 2, math.pi / 2),
        Rotation(0, 1, math.pi / 2),
    ]
    
    result_a = point
    
    for rotation in first_xy_then_xz:
        result_a = rotate_plane(
            result_a,
            rotation.i,
            rotation.j,
            rotation.angle,
        )
    
    result_b = point
    
    for rotation in first_xz_then_xy:
        result_b = rotate_plane(
            result_b,
            rotation.i,
            rotation.j,
            rotation.angle,
        )
    
    assert result_a != result_b

def test_apply_rotations_preserves_order():
    point = [1, 1, 0]
    
    rotations = [
        Rotation(0, 1, math.pi / 2),
        Rotation(0, 2, math.pi / 2),
    ]
    
    result = apply_rotations(point, rotations)
    
    expected = [0, 1, -1]
    
    for actual, target in zip(result, expected):
        assert math.isclose(actual, target, abs_tol=1e-9)

def test_apply_rotations_does_not_modify_original():
    point = [1, 2, 3, 4]
    
    rotations = [
        Rotation(0, 1, math.pi / 2),
        Rotation(2, 3, math.pi / 4),
    ]
    
    apply_rotations(point, rotations)
    
    assert point == [1, 2, 3, 4]

def test_zero_rotation():
    point = [1.5, -2.0, 3.7, 4.2]
    
    result = rotate_plane(point, 1, 3, 0)
    
    assert result == point

def test_full_rotation():
    point = [1.5, -2.0, 3.7, 4.2]
    
    result = rotate_plane(point, 0, 2, 2 * math.pi)
    
    for actual, expected in zip(result, point):
        assert math.isclose(actual, expected, abs_tol=1e-9)

def test_rotation_preserves_length():
    point = [1.5, -2.0, 3.7, 4.2, -0.8]
    
    result = rotate_plane(point, 1, 4, math.pi / 3)
    
    original_length = math.sqrt(sum(x**2 for x in point))
    rotated_length = math.sqrt(sum(x**2 for x in result))
    
    assert math.isclose(
        rotated_length,
        original_length,
        abs_tol=1e-9,
    )

def test_rotation_leaves_other_coordinates_unchanged():
    point = [1.5, -2.0, 3.7, 4.2, -0.8]
    
    result = rotate_plane(point, 0, 3, math.pi / 4)
    
    assert result[1] == point[1]
    assert result[2] == point[2]
    assert result[4] == point[4]

def test_same_plane_rotations_add_angles():
    point = [1.2, -0.7, 3.4, 2.1]
    
    first = rotate_plane(point, 0, 2, math.pi / 6)
    first = rotate_plane(first, 0, 2, math.pi / 4)
    
    combined = rotate_plane(point, 0, 2, 5 * math.pi / 12)
    
    for actual, expected in zip(first, combined):
        assert math.isclose(actual, expected, abs_tol=1e-9)

def test_rotation_and_inverse():
    point = [1.2, -0.7, 3.4, 2.1]
    
    result = rotate_plane(point, 1, 3, math.pi / 5)
    result = rotate_plane(result, 1, 3, -math.pi / 5)
    
    for actual, expected in zip(result, point):
        assert math.isclose(actual, expected, abs_tol=1e-9)

def test_rotation_of_zero_point():
    point = [0, 0, 0, 0, 0, 0]
    
    result = rotate_plane(point, 2, 5, 1.234)
    
    assert result == point

def test_same_plane_rotations_commute():
    point = [1.2, -0.7, 3.4, 2.1]
    
    first = rotate_plane(point, 0, 2, math.pi / 6)
    first = rotate_plane(first, 0, 2, math.pi / 4)
    
    second = rotate_plane(point, 0, 2, math.pi / 4)
    second = rotate_plane(second, 0, 2, math.pi / 6)
    
    for actual, expected in zip(first, second):
        assert math.isclose(actual, expected, abs_tol=1e-9)

def test_different_plane_rotations_do_not_commute():
    point = [1, 1, 0]
    
    first = rotate_plane(point, 0, 1, math.pi / 2)
    first = rotate_plane(first, 0, 2, math.pi / 2)
    
    second = rotate_plane(point, 0, 2, math.pi / 2)
    second = rotate_plane(second, 0, 1, math.pi / 2)
    
    assert first != second

def test_rotation_rejects_same_coordinate():
    point = [1, 2, 3]
    
    with pytest.raises(ValueError):
        rotate_plane(point, 1, 1, math.pi / 4)

def test_rotation_rejects_out_of_range_index():
    point = [1, 2, 3]
    
    with pytest.raises(IndexError):
        rotate_plane(point, 0, 3, math.pi / 4)

def test_rotation_rejects_negative_index():
    point = [1, 2, 3]
    
    with pytest.raises(IndexError):
        rotate_plane(point, -1, 1, math.pi / 4)

def test_rotation_rejects_non_integer_index():
    point = [1, 2, 3]
    
    with pytest.raises(TypeError):
        rotate_plane(point, 0.5, 2, math.pi / 4)

def test_rotation_rejects_non_integer_second_index():
    point = [1, 2, 3]
    
    with pytest.raises(TypeError):
        rotate_plane(point, 0, 1.5, math.pi / 4)

def test_apply_empty_rotation_sequence():
    point = [1, 2, 3, 4]
    
    result = apply_rotations(point, [])
    
    assert result == point
    assert result is not point

def test_apply_single_rotation():
    point = [1, 0, 0, 0]
    
    rotation = Rotation(0, 3, math.pi / 2)
    
    result = apply_rotations(point, [rotation])
    
    expected = [0, 0, 0, 1]
    
    for actual, target in zip(result, expected):
        assert math.isclose(actual, target, abs_tol=1e-9)

def test_apply_multiple_rotations():
    point = [1, 1, 0, 0]
    
    rotations = [
        Rotation(0, 1, math.pi / 2),
        Rotation(2, 3, math.pi / 2),
        Rotation(0, 2, math.pi / 2),
    ]
    
    result = apply_rotations(point, rotations)
    
    expected = [0, 1, -1, 0]
    
    for actual, target in zip(result, expected):
        assert math.isclose(actual, target, abs_tol=1e-9)
