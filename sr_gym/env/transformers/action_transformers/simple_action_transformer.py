from gymnasium.spaces import Dict, MultiBinary

from sr_gym.ipc.packet import GameState, PlayerInput
from sr_gym.env.transformers.action_transformers import ActionTransformer

class SimpleActionTransformer(ActionTransformer):
    """
    The simplest action transformer, just returning the underlying action.
    """
    def __init__(self):
        """
        Creates the simple action transformer.
        """
        super().__init__()

        self._action_space: Dict = Dict({
            "left": MultiBinary(1),
            "right": MultiBinary(1),
            "jump": MultiBinary(1),
            "grapple": MultiBinary(1),
            "weapon": MultiBinary(1),
            "item": MultiBinary(1),
            "taunt": MultiBinary(1),
            "swap_weapon": MultiBinary(1),
            "slide": MultiBinary(1),
            "boost": MultiBinary(1),
        })

    def reset(self, initial_state: GameState) -> None:
        """
        Resets the action transformer, effectively doing nothing.

        Args:
            initial_state: The initial state of the environment to reset to.
        """
        # Nothing needs to be done
        return

    def transform_action(self, action: PlayerInput) -> PlayerInput:
        """
        Returns the action.

        Args:
            action: The action to transform.
        
        Returns:
            The same input action.
        """
        return action

    def action_space(self) -> Dict:
        """
        The action space of the pre-transformed input action.

        Returns:
            The action space of the pre-transformed input action.
        """
        return self._action_space
