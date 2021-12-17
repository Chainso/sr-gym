from dataclasses import dataclass

from dataclasses_json import dataclass_json

from .entity import Entity

@dataclass
@dataclass_json
class Player:
    """
    A game player.
    """
    entity: Entity
    grapple_radius: float
    grapple_angle: float
    boost: float
    lap_time: float
    sliding: bool
    swinging: bool
    in_air: bool
    on_ground: bool
    item: int
    last_move_direction: int

