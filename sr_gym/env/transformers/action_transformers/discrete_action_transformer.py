from gymnasium.spaces import Discrete

from sr_gym.env.transformers.action_transformers.one_hot_discrete_action_transformer import (
    OneHotDiscreteActionTransformer
)

class DiscreteActionTransformer(OneHotDiscreteActionTransformer):
    """
    An action transformer using preset discrete actions.
    """
    def __init__(self):
        """
        Creates the discrete action transformer.
        """
        super().__init__()
        self._action_space = Discrete(self.action_space().shape[0])
