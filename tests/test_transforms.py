import math

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
