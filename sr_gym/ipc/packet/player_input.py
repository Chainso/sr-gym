from dataclasses import dataclass
from typing import ClassVar

from sr_gym.ipc.packet.dataclass import dataclass_json

@dataclass_json
@dataclass
class PlayerInput:
    """
    The inputs for a game player.
    """
    num_inputs: ClassVar[int] = 10

    left: bool = False
    right: bool = False
    jump: bool = False
    grapple: bool = False
    weapon: bool = False
    item: bool = False
    taunt: bool = False
    swap_weapon: bool = False
    slide: bool = False
    boost: bool = False
