from typing import Any, Dict, List, Tuple

from gym import Env

from sr_gym.ipc import Connection

class SRGym(Env):
    """
    A gym environment for SpeedRunners.
    """
    def __init__(self, connection: Connection):
        """
        Creates the gym environment using an existing connection.

        Args:
            connection: The connection to get packets from.
        """
        self.connection = connection

    def reset(self) -> None:
        """
        Resets the SpeedRunners game and current lap.
        """
        raise NotImplementedError

    def step(self, action: Tuple[Any, ...]) -> Tuple[List, float, bool, Dict]:
        """
        Takes one step in the SpeedRunners game, executing the action.

        Args:
            action: The action to execute.
        """
        raise NotImplementedError

    def close(self) -> None:
        """
        Closes the gym environment.
        """
        self.connection.close()
