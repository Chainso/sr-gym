from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from .game_info import GameInfo
from .player import Player

@dataclass
class Game:
    """
    All data about the game.
    """
    info: GameInfo
    players: List[Player]
