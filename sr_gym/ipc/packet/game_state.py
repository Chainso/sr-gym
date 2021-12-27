from dataclasses import dataclass
from typing import List

from sr_gym.ipc.packet.dataclass import dataclass_json

from .game_info import GameInfo
from .player import Player

@dataclass_json
@dataclass
class GameState:
    """
    All data about the game.
    """
    info: GameInfo
    players: List[Player]
