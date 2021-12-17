from dataclasses import dataclass

from dataclasses_json import dataclass_json

from .vector2 import Vector2

@dataclass
@dataclass_json
class Entity:
    """
    A generic game entity.
    """
    position: Vector2
    velocity: Vector2
