import math

from python_task.shapes.shape import IShape


class Triangle(IShape):
    """
    Represents a triangle defined by three sides,
    and provides methods to calculate area and check if it is a right triangle.

    Attributes:
        a (float): Length of side a.
        b (float): Length of side b.
        c (float): Length of side c.
    """

    def __init__(self, a: float, b: float, c: float):
        """
        The constructor of class.

        Args:
            a (float): Side a.
            b (float): Side b.
            c (float): Side c.

        Raises:
            ValueError: If the given sides do not form a valid triangle.
        """
        self.a = a
        self.b = b
        self.c = c
        if not self._is_valid_triangle():
            raise ValueError("Invalid triangle sides")

    def area(self) -> float:
        """
        Calculates the area of the triangle using Heron's formula,
        where p is the semi-perimeter.

        Returns:
            float: The area of the triangle.
        """
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        """
        Checks if the triangle is a right triangle using the Pythagorean theorem.

        Returns:
            bool: True if the triangle is right-angled, False otherwise.
        """
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)

    def _is_valid_triangle(self) -> bool:
        """
        Checks whether the sides satisfy the triangle inequality theorem.

        Returns:
            bool: True if the sides form a valid triangle, False otherwise.
        """
        a, b, c = self.a, self.b, self.c
        return a + b > c and a + c > b and b + c > a
