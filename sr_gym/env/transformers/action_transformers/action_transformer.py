from abc import ABC, abstractmethod
from typing import Any

from gymnasium.spaces import Space

from sr_gym.ipc.packet import GameState, PlayerInput

class ActionTransformer(ABC):
    """
    An abstract action transformer.
    """
    @abstractmethod
    def reset(self, initial_state: GameState) -> None:
        """
        Resets the action transformer using the initial state.

        Args:
            initial_state: The initial state of the environment being reset to.
        """
        raise NotImplementedError

    @abstractmethod
    def transform_action(self, action: Any) -> PlayerInput:
        """
        Transforms a single action.

        Args:
            action: The action to transform.
        
        Returns:
            The transformed action.
        """
        raise NotImplementedError

    @abstractmethod
    def action_space(self) -> Space:
        """
        The action space of the pre-transformed input action.

        Returns:
            The action space of the pre-transformed input action.
        """
        raise NotImplementedError
