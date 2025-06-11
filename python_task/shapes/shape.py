from abc import ABC, abstractmethod

class IShape(ABC):
    """
    Abstract base class for geometric shapes.
    Defines the interface for area calculation.
    """

    @abstractmethod
    def area(self) -> float:
        """
        Abstract method to calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass