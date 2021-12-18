from dataclasses import dataclass

from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class GameInfo:
    """
    Game specific data.
    """
    lap_time: float

