import math
from dataclasses import dataclass

from dataclasses_json import dataclass_json

@dataclass
@dataclass_json
class Vector2:
    """
    A 2 dimensional vector.
    """
    x: float
    y: float

    def length(self) -> float:
        """
        Calculates the length of the vector.

        Returns:
            The vector length (magnitude).
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)
