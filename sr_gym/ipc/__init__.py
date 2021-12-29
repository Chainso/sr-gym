from typing import Final

from .connection import Connection

MAX_MESSAGE_SIZE: Final[int] = 1024

__all__ = [
    "Connection",
    "MAX_MESSAGE_SIZE"
]
