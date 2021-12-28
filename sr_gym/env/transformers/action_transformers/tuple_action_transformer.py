import numpy as np
from gym.spaces import MultiBinary

from sr_gym.ipc.packet import GameState, PlayerInput
from sr_gym.env.transformers.action_transformers import ActionTransformer

class TupleActionTransformer(ActionTransformer):
    """
    An action transformer taking the player inputs as a tuple of booleans.
    """
    def __init__(self):
        """
        Creates the tuple action transformer.
        """
        super().__init__()

        self._action_space: MultiBinary = MultiBinary(PlayerInput.num_inputs)

    def reset(self, initial_state: GameState) -> None:
        """
        Resets the action transformer, effectively doing nothing.

        Args:
            initial_state: The initial state of the environment to reset to.
        """
        # Nothing needs to be done
        return

    def transform_action(
            self,
            action: tuple[(bool,) * PlayerInput.num_inputs]
        ) -> PlayerInput:
        """
        Transformers the action array into player input object.

        Args:
            action: The action to transform.
        
        Returns:
            The player input object action.
        """
        return PlayerInput(*np.array(action).astype(bool))

    def action_space(self) -> MultiBinary:
        """
        The action space of the pre-transformed input action.

        Returns:
            The action space of the pre-transformed input action.
        """
        return self._action_space
