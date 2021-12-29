from typing import Final

from .connection import Connection

DEFAULT_PIPE_NAME: Final[str] = "\\\\.\\pipe\\SpeedRunners-lib"
MAX_MESSAGE_SIZE: Final[int] = 1024

__all__ = [
    "Connection",
    "MAX_MESSAGE_SIZE"
]
