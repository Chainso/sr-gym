from abc import ABC, abstractmethod
from typing import Any

from gym.spaces import Space

from sr_gym.ipc.packet import GameState

class StateTransformer(ABC):
    """
    An abstract state transformer.
    """
    @abstractmethod
    def reset(self, initial_state: GameState) -> Any:
        """
        Resets the state transformer using the initial state.

        Args:
            initial_state: The initial state of the environment to reset to.

        Returns:
            The transformed initial state.
        """
        raise NotImplementedError

    @abstractmethod
    def transform_state(self, state: GameState) -> Any:
        """
        Transforms a single state.

        Args:
            state: The state to transform.
        
        Returns:
            The transformed state.
        """
        raise NotImplementedError

    @abstractmethod
    def state_space(self) -> Space:
        """
        The state space of the transformed state.

        Returns:
            The state space of the transformed state.
        """
        raise NotImplementedError
