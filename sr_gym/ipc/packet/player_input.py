from dataclasses import dataclass
from typing import ClassVar

from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class PlayerInput:
    """
    The inputs for a game player.
    """
    num_inputs: ClassVar[int] = 10

    left: bool
    right: bool
    jump: bool
    grapple: bool
    weapon: bool
    item: bool
    taunt: bool
    swap_weapon: bool
    slide: bool
    boost: bool
