from gym.spaces import MultiBinary

from sr_gym.ipc.packet import GameState
from sr_gym.ipc.packet import PlayerInput
from sr_gym.env.transformers.action_transformers import ActionTransformer
from sr_gym.env.spaces import TupleShaped

class TupleActionTransformer(ActionTransformer):
    """
    The simplest action transformer, just returning the underlying action.
    """
    def __init__(self, num_players: int = 1):
        """
        Creates the tuple action transformer for the number of players.

        Args:
            num_players: The number of players in the environment.
        """
        self._action_space: TupleShaped = TupleShaped(tuple(
            MultiBinary(PlayerInput.num_inputs) for _ in range(num_players)
        ))

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
        return PlayerInput(*action)

    def action_space(self) -> TupleShaped:
        """
        The action space of the pre-transformed input action.

        Returns:
            The action space of the pre-transformed input action.
        """
        return self._action_space
