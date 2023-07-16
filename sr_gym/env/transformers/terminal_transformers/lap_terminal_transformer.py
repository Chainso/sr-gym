from typing import Any, Dict, Optional

from sr_gym.ipc.packet import GameState, PlayerInput
from sr_gym.env.transformers.terminal_transformers import TerminalTransformer

class LapTerminalTransformer(TerminalTransformer):
    """
    Calculates if a new state is terminal based on the time of the current lap.
    """
    def __init__(self, max_time: Optional[float] = None):
        """
        Create the terminal transformer, resetting when a lap is finish, or
        when the max time has been achieved.

        Args:
            max_time: The maximum time per lap before a terminal is reached.
        """
        super().__init__()

        if max_time is not None and max_time <= 0:
            raise ValueError(
                "The maximum lap time ({0}) must be greater than 0".format(
                    max_time
                )
            )

        self.max_time = max_time

    def reset(self, initial_state: GameState) -> None:
        """
        Resets the terminal transformer using the initial state.

        Args:
            initial_state: The initial state of the environment to reset to.
        """   
        return

    def transform_terminal(
            self,
            state: GameState,
            action: PlayerInput,
            next_state: GameState,
            info: Dict[str, Any]
        ) -> bool:
        """
        Transforms a single terminal based on the lap.

        Args:
            state: The state before the action was taken.
            action: The action that was taken.
            next_state: The state after the action was taken.
            info: A dictionary of additional information of the environment,
                and to add more information to.
        
        Returns:
            True if the this state transition has been determined has resulted
            in the new state being terminal.
        """
        # Check if the current lap time is less than the current one, indicates
        # that this is a new lap
        real_finish = state.info.lap_time > next_state.info.lap_time
        timeout = (
            False if self.max_time is None
            else state.info.lap_time >= self.max_time
        )

        info["TimeLimit.truncated"] = timeout and not real_finish

        return real_finish
