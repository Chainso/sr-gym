from abc import ABC, abstractmethod

from sr_gym.ipc.packet import GameState
from sr_gym.ipc.packet import PlayerInput

class RewardTransformer(ABC):
    """
    An abstract reward transformer.
    """
    @abstractmethod
    def reset(self, initial_state: GameState) -> None:
        """
        Resets the reward transformer using the initial state.

        Args:
            initial_state: The initial state of the environment being reset to.
        """
        raise NotImplementedError

    @abstractmethod
    def transform_reward(
            self,
            state: GameState,
            action: PlayerInput,
            next_state: GameState,
            terminal: bool
        ) -> float:
        """
        Transforms a single reward.

        Args:
            state: The state before the action was taken.
            action: The action that was taken.
            next_state: The state after the action was taken.
            terminal: If the new state is a terminal state.
        
        Returns:
            The calculated reward.
        """
        raise NotImplementedError
