from dataclasses import dataclass

from dataclasses_json import dataclass_json

@dataclass
@dataclass_json
class GameInfo:
    """
    Game specific data.
    """
    lap_time: float

