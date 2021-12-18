from dataclasses import dataclass

from dataclasses_json import dataclass_json

from sr_gym.ipc.packet.entity import Entity
from sr_gym.ipc.packet.player_input import PlayerInput

@dataclass_json
@dataclass
class Player:
    """
    A game player.
    """
    entity: Entity
    grapple_radius: float
    grapple_angle: float
    boost: float
    input: PlayerInput
    in_air: bool
    sliding: bool
    sliding_on_ground: bool
    grappling: bool
    on_wall: bool
    on_ground: bool
    item: int
    last_move_direction: int
