from .shapes.shape import IShape

def compute_area(shape: IShape) -> float:
    """
    Computes the area of any shape that implements the Shape interface.

    Args:
        shape (Shape): An instance of a class that implements the area() method.

    Returns:
        float: The computed area of the shape.
    """
    return shape.area()