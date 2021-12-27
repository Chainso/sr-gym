from dataclasses import dataclass

from sr_gym.ipc.packet.dataclass import dataclass_json

@dataclass_json
@dataclass
class GameInfo:
    """
    Game specific data.
    """
    lap_time: float

