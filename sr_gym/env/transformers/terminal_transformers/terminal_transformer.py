from abc import ABC, abstractmethod

from sr_gym.ipc.packet import GameState
from sr_gym.ipc.packet import PlayerInput

class TerminalTransformer(ABC):
    """
    An abstract terminal transformer.
    """
    @abstractmethod
    def reset(self, initial_state: GameState) -> None:
        """
        Resets the terminal transformer using the initial state.

        Args:
            initial_state: The initial state of the environment being reset to.
        """
        raise NotImplementedError

    @abstractmethod
    def transform_terminal(
            self,
            state: GameState,
            action: PlayerInput,
            next_state: GameState
        ) -> bool:
        """
        Transforms a single terminal.

        Args:
            state: The state before the action was taken.
            action: The action that was taken.
            next_state: The state after the action was taken.
        
        Returns:
            True if the this state transition has been determined has resulted
            in the new state being terminal.
        """
        raise NotImplementedError
