from sr_gym.ipc.packet import GameState, PlayerInput
from sr_gym.env.transformers.action_transformers import ActionTransformer
from sr_gym.env.spaces import OneHotDiscreteShaped

class DiscreteActionTransformer(ActionTransformer):
    """
    An action transformer using preset discrete actions.
    """
    ACTIONS = (
        PlayerInput(left=True),
        PlayerInput(left=True, boost=True),
        PlayerInput(left=True, jump=True),
        PlayerInput(left=True, jump=True, boost=True),
        PlayerInput(left=True, grapple=True),
        PlayerInput(left=True, grapple=True, boost=True),
        PlayerInput(right=True),
        PlayerInput(right=True, boost=True),
        PlayerInput(right=True, jump=True),
        PlayerInput(right=True, jump=True, boost=True),
        PlayerInput(right=True, grapple=True),
        PlayerInput(right=True, grapple=True, boost=True),
        PlayerInput(slide=True)
    )

    def __init__(self):
        """
        Creates the discrete action transformer.
        """
        super().__init__()

        self._action_space: OneHotDiscreteShaped = OneHotDiscreteShaped(
            len(DiscreteActionTransformer.ACTIONS)
        )

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
            action: int
        ) -> PlayerInput:
        """
        Selects the action corresponding to the index given.

        Args:
            action: The action to perform.
        
        Returns:
            The player input that corresponds to the action index.
        """
        return DiscreteActionTransformer.ACTIONS[action]

    def action_space(self) -> OneHotDiscreteShaped:
        """
        The action space of the pre-transformed input action.

        Returns:
            The action space of the pre-transformed input action.
        """
        return self._action_space
