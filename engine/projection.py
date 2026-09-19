from dataclasses import dataclass


@dataclass(frozen=True)
class Projection:
    axis: int
    distance: float
    projection: float


def project_point(point, axis, distance, projection):
    """
    Project an N-dimensional point into N-1 dimensions.
    
    The selected coordinate defines the projection depth and is removed from the resulting N-1 dimensional point.
    The input point is not modified.
    
    Raises:
        TypeError: If axis is not an integer.
        IndexError: If axis is negative or out of range.
        ValueError: If the projection is undefined at the projection center.
    """
    
    if not isinstance(axis, int):
        raise TypeError("Projection axis must be an integer.")
    
    if axis < 0 or axis >= len(point):
        raise IndexError("Projection axis out of range.")
    
    denominator = distance - point[axis]
    
    if denominator == 0:
        raise ValueError("Projection is undefined at the projection center.")
    
    scale = projection / denominator
    
    return [
        coordinate * scale
        for index, coordinate in enumerate(point)
        if index != axis
    ]

def apply_projections(point, projections):
    """
    Apply a sequence of projections to an N-dimensional point.
    
    Projections are applied in the exact order provided.
    Each projection reduces the dimensionality by one.
    The input point is not modified.
    """
    
    result = point.copy()
    
    for projection in projections:
        result = project_point(
            result,
            projection.axis,
            projection.distance,
            projection.projection,
        )
    
    return result
