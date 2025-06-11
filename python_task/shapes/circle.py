import math

from python_task.shapes.shape import IShape


class Circle(IShape):
    """
    Represents a circle and provides a method to calculate its area.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius: float):
        """
        The constructor of class.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self) -> float:
        """
        Calculates the area of the circle using the formula π * r^2.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2