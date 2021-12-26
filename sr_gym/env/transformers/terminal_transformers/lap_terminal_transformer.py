from sr_gym.ipc.packet import GameState
from sr_gym.ipc.packet import PlayerInput
from sr_gym.env.transformers.terminal_transformers import TerminalTransformer

class LapTerminalTransformer(TerminalTransformer):
    """
    Calculates a reward based on the velocity of the player.
    """
    def __init__(self):
        """
        Creates the terminal transformer.
        """
        self.lap_time = 0

    def reset(self, initial_state: GameState) -> None:
        """
        Resets the terminal transformer using the initial state.

        Args:
            initial_state: The initial state of the environment to reset to.
        """   
        self.lap_time = initial_state.info.lap_time

    def transform_terminal(
            self,
            state: GameState,
            action: PlayerInput,
            next_state: GameState
        ) -> bool:
        """
        Transforms a single terminal based on the lap.

        Args:
            state: The state before the action was taken.
            action: The action that was taken.
            next_state: The state after the action was taken.
        
        Returns:
            True if the this state transition has been determined has resulted
            in the new state being terminal.
        """
        # Check if the current lap time is less than the current one, indicates
        # that this is a new lap
        new_lap_time = next_state.info.lap_time
        terminal = new_lap_time < self.lap_time
        self.lap_time = new_lap_time

        return terminal
