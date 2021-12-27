from dataclasses import dataclass

from sr_gym.ipc.packet.dataclass import dataclass_json

from .vector2 import Vector2

@dataclass_json
@dataclass
class Entity:
    """
    A generic game entity.
    """
    position: Vector2
    velocity: Vector2
