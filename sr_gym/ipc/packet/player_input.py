from dataclasses import dataclass

from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class PlayerInput:
    """
    The inputs for a game player.
    """
    left: bool
    right: bool
    jump: bool
    grapple: bool
    item: bool
    taunt: bool
    swap_weapon: bool
    slide: bool
    boost: bool
