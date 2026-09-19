import math

from engine.transforms import rotate_plane


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