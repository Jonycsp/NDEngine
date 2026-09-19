import math
import pytest
from engine.projection import (
    Projection,
    apply_projections,
    project_point,
)

def test_projection_removes_selected_axis():
    point = [1, 2, 3, 4]
    
    result = project_point(
        point,
        axis=3,
        distance=5,
        projection=1,
    )
    
    expected = [1, 2, 3]
    
    for actual, target in zip(result, expected):
        assert math.isclose(actual, target, abs_tol=1e-9)

def test_projection_can_remove_middle_axis():
    point = [2, 4, 6, 8]
    
    result = project_point(
        point,
        axis=1,
        distance=10,
        projection=1,
    )
    
    expected = [1 / 3, 1, 4 / 3]
    
    for actual, target in zip(result, expected):
        assert math.isclose(actual, target, abs_tol=1e-9)

def test_projection_uses_projection_parameter():
    point = [2, 4, 6]
    
    result = project_point(
        point,
        axis=2,
        distance=10,
        projection=2,
    )
    
    expected = [1, 2]
    
    for actual, target in zip(result, expected):
        assert math.isclose(actual, target, abs_tol=1e-9)

def test_projection_does_not_modify_original():
    point = [1, 2, 3, 4]
    
    project_point(
        point,
        axis=2,
        distance=10,
        projection=1,
    )
    
    assert point == [1, 2, 3, 4]

def test_projection_reduces_dimension_by_one():
    point = [1, 2, 3, 4, 5, 6]
    
    result = project_point(
        point,
        axis=3,
        distance=10,
        projection=1,
    )
    
    assert len(result) == len(point) - 1

def test_projection_rejects_singularity():
    point = [1, 2, 5]
    
    with pytest.raises(ValueError):
        project_point(
            point,
            axis=2,
            distance=5,
            projection=1,
        )

def test_projection_allows_near_singularity():
    point = [1.0, 0.0, 5.0 - 1e-6]
    
    result = project_point(
        point,
        axis=2,
        distance=5.0,
        projection=1.0,
    )
    
    assert math.isclose(result[0], 1e6)
    assert result[1] == 0.0

def test_projection_rejects_negative_axis():
    point = [1.0, 2.0, 3.0]
    
    with pytest.raises(IndexError):
        project_point(
            point,
            axis=-1,
            distance=5.0,
            projection=1.0,
        )

def test_projection_rejects_out_of_range_axis():
    point = [1.0, 2.0, 3.0]
    
    with pytest.raises(IndexError):
        project_point(
            point,
            axis=3,
            distance=5.0,
            projection=1.0,
        )

def test_projection_rejects_non_integer_axis():
    point = [1.0, 2.0, 3.0]
    
    with pytest.raises(TypeError):
        project_point(
            point,
            axis=1.5,
            distance=5.0,
            projection=1.0,
        )

def test_projection_allows_axis_zero():
    point = [2.0, 4.0, 6.0]
    
    result = project_point(
        point,
        axis=0,
        distance=5.0,
        projection=1.0,
    )
    
    assert result == [4.0 / 3.0, 2.0]

def test_projection_with_zero_projection_parameter():
    point = [1.0, 2.0, 3.0]
    
    result = project_point(
        point,
        axis=2,
        distance=5.0,
        projection=0.0,
    )
    
    assert result == [0.0, 0.0]

def test_projection_preserves_sign():
    point = [1.0, 0.0, 6.0]
    
    result = project_point(
        point,
        axis=2,
        distance=5.0,
        projection=1.0,
    )
    
    assert result == [-1.0, 0.0]

def test_projection_can_project_to_one_dimension():
    point = [2.0, 4.0]
    
    result = project_point(
        point,
        axis=0,
        distance=5.0,
        projection=1.0,
    )
    
    assert result == [4.0 / 3.0]

def test_projection_can_project_a_two_dimensional_point():
    point = [2.0, 4.0]
    
    result = project_point(
        point,
        axis=1,
        distance=6.0,
        projection=2.0,
    )
    
    assert result == [2.0]

def test_projection_scales_with_projection_parameter():
    point = [2.0, 4.0, 1.0]
    
    result_1 = project_point(
        point,
        axis=2,
        distance=5.0,
        projection=1.0,
    )
    
    result_2 = project_point(
        point,
        axis=2,
        distance=5.0,
        projection=2.0,
    )
    
    assert result_2 == [2 * coordinate for coordinate in result_1]

def test_projection_removes_only_selected_coordinate():
    point = [10.0, 20.0, 30.0, 40.0]
    
    result = project_point(
        point,
        axis=1,
        distance=100.0,
        projection=1.0,
    )
    
    assert len(result) == 3
    assert result != point
    assert result[0] == 10.0 / 80.0
    assert result[1] == 30.0 / 80.0
    assert result[2] == 40.0 / 80.0

def test_projection_representation():
    projection = Projection(
        axis=3,
        distance=5.0,
        projection=1.0,
    )
    
    assert projection.axis == 3
    assert projection.distance == 5.0
    assert projection.projection == 1.0

def test_apply_projections_with_one_projection():
    point = [1.0, 2.0, 3.0, 4.0]
    
    projections = [
        Projection(
            axis=3,
            distance=5.0,
            projection=1.0,
        )
    ]
    
    result = apply_projections(point, projections)
    
    assert result == [1.0, 2.0, 3.0]

def test_apply_projections_multiple_dimensions():
    point = [1.0, 0.0, 0.0, -1.0]
    
    projections = [
        Projection(
            axis=3,
            distance=2.0,
            projection=1.0,
        ),
        Projection(
            axis=2,
            distance=2.0,
            projection=1.0,
        ),
    ]
    
    result = apply_projections(point, projections)
    
    assert result == [1.0 / 6.0, 0.0]

def test_apply_projections_does_not_modify_original():
    point = [1.0, 2.0, 3.0, 4.0]
    original = point.copy()
    
    projections = [
        Projection(
            axis=3,
            distance=5.0,
            projection=1.0,
        ),
        Projection(
            axis=2,
            distance=5.0,
            projection=1.0,
        ),
    ]
    
    apply_projections(point, projections)
    
    assert point == original

def test_projection_order_matters():
    point = [1.0, 2.0, 3.0, 4.0]
    
    first_order = [
        Projection(axis=3, distance=10.0, projection=1.0),
        Projection(axis=2, distance=10.0, projection=1.0),
    ]
    
    second_order = [
        Projection(axis=2, distance=10.0, projection=1.0),
        Projection(axis=2, distance=10.0, projection=1.0),
    ]
    
    result_first = apply_projections(point, first_order)
    result_second = apply_projections(point, second_order)
    
    assert result_first != result_second

def test_apply_projections_rejects_invalid_axis_after_dimension_reduction():
    point = [1.0, 2.0, 3.0, 4.0]
    
    projections = [
        Projection(axis=3, distance=10.0, projection=1.0),
        Projection(axis=3, distance=10.0, projection=1.0),
    ]
    
    with pytest.raises(IndexError):
        apply_projections(point, projections)

def test_apply_projections_with_empty_sequence():
    point = [1.0, 2.0, 3.0]
    
    result = apply_projections(point, [])
    
    assert result == point
    assert result is not point

def test_apply_projections_from_five_dimensions_to_two():
    point = [1.0, 2.0, 3.0, 4.0, 5.0]
    
    projections = [
        Projection(axis=4, distance=10.0, projection=1.0),
        Projection(axis=3, distance=10.0, projection=1.0),
        Projection(axis=2, distance=10.0, projection=1.0),
    ]
    
    result = apply_projections(point, projections)
    
    assert len(result) == 2


