import unittest
from python_task.shapes.circle import Circle
from python_task.shapes.triangle import Triangle
from python_task.utils import compute_area
import math


class TestGeometry(unittest.TestCase):
    """
    Unit tests for Circle and Triangle shape classes and the compute_area utility function.
    """

    def test_circle_area(self):
        """
        Test that the area of a circle with radius 1 is approximately π.
        """
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), math.pi)

    def test_triangle_area(self):
        """
        Test that the area of a triangle with sides 3, 4, 5 is 6 (Heron's formula).
        """
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_right_triangle(self):
        """
        Test that a triangle with sides 3, 4, 5 is correctly identified as right-angled.
        """
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right())

    def test_non_right_triangle(self):
        """
        Test that a triangle with sides 3, 4, 6 is not right-angled.
        """
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right())

    def test_invalid_triangle(self):
        """
        Test that a triangle with invalid sides raises a ValueError.
        """
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)  # violates triangle inequality

    def test_compute_area_polymorphism(self):
        """
        Test that the compute_area function works correctly using polymorphism.
        """
        shapes = [Circle(1), Triangle(3, 4, 5)]
        areas = [compute_area(s) for s in shapes]
        self.assertAlmostEqual(areas[0], math.pi)
        self.assertAlmostEqual(areas[1], 6.0)


if __name__ == "__main__":
    unittest.main()
