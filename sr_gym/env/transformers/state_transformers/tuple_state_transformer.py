from typing import Any, Tuple

import numpy as np
from gymnasium.spaces import Box, MultiBinary

from sr_gym.ipc.packet import GameState
from sr_gym.env.transformers.state_transformers import StateTransformer
from sr_gym.env.spaces import DiscreteShaped, TupleShaped

class TupleStateTransformer(StateTransformer):
    """
    The state as a flat tuple of individual spaces.
    """
    def __init__(self, num_players: int = 1):
        """
        Creates the state transformer for the number of players.

        Args:
            num_players: The number of players in the environment.
        """
        super().__init__()

        if num_players <= 0:
            raise ValueError(
                "The number of players ({0}) must be greater than 0".format(
                    num_players
                )
            )

        game_info_space = [
            Box(low=0, high=np.inf, shape=(1,))
        ]

        players_info_space = []

        for _ in range(num_players):
            player_info_space = [
                Box(low=np.NINF, high=np.inf, shape=(2,)),
                Box(low=np.NINF, high=np.inf, shape=(2,)),
                Box(low=0, high=np.inf, shape=(1,)),
                Box(low=-2 * np.pi, high=2 * np.pi, shape=(1,)),
                Box(low=0, high=2, shape=(1,)),
                MultiBinary(1),
                MultiBinary(1),
                MultiBinary(1),
                MultiBinary(1),
                MultiBinary(1),
                MultiBinary(1),
                DiscreteShaped(20),
                Box(low=-1, high=1, shape=(1,))
            ]
            players_info_space += player_info_space

        self._state_space: TupleShaped = TupleShaped(
            game_info_space + players_info_space
        )

    def reset(self, initial_state: GameState) -> GameState:
        """
        Returns the initial state.

        Args:
            initial_state: The initial state of the environment to reset to.

        Returns:
            The initial state.
        """
        return self.transform_state(initial_state)

    def transform_state(self, state: GameState) -> Tuple[Any, ...]:
        """
        Returns the state.

        Args:
            state: The state to transform.
        
        Returns:
            A flat tuple representing the game state.
        """
        game_info = [state.info.lap_time]

        players = []

        for player in state.players:
            player_state = (
                [player.entity.position.x, player.entity.position.y]
                + [player.entity.velocity.x, player.entity.velocity.y]
                + [player.grapple_radius]
                + [player.grapple_angle]
                + [player.boost]
                + [player.in_air]
                + [player.sliding]
                + [player.sliding_on_ground]
                + [player.grappling]
                + [player.on_wall]
                + [player.on_ground]
                + [player.item]
                + [player.last_move_direction]
            )
            players += player_state

        state = game_info + players

        return np.array(state)

    def state_space(self) -> TupleShaped:
        """
        The state space of the transformed state.

        Returns:
            The state space of the transformed state.
        """
        return self._state_space
