import math


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