import numpy as np
from gymnasium.spaces import Box

from sr_gym.env.transformers.state_transformers.tuple_state_transformer import (
    TupleStateTransformer
)

class FlattenedTupleStateTransformer(TupleStateTransformer):
    """
    The state as a flat tuple of individual spaces.
    """
    def __init__(self, num_players: int = 1):
        """
        Creates the state transformer for the number of players.

        Args:
            num_players: The number of players in the environment.
        """
        super().__init__(num_players)

        state_size = np.sum(self.state_space().shape)
        self._state_space = Box(low=np.NINF, high=np.inf, shape=(state_size,))
