import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Rotation:
    i: int
    j: int
    angle: float


def rotate_plane(point, i, j, angle):
    """
    Rotate an N-dimensional point in the plane defined by coordinates i and j.
    
    The input point is not modified. A new point is returned.
    """
    
    rotated = point.copy()
    
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    
    xi = point[i]
    xj = point[j]
    
    rotated[i] = xi * cos_theta - xj * sin_theta
    rotated[j] = xi * sin_theta + xj * cos_theta
    
    return rotated

def apply_rotations(point, rotations):
    """
    Apply a sequence of rotations to an N-dimensional point.
    
    Rotations are applied in the exact order provided.
    The input point is not modified.
    """
    
    result = point.copy()
    
    for rotation in rotations:
        result = rotate_plane(
            result,
            rotation.i,
            rotation.j,
            rotation.angle,
        )
    
    return result