import numpy as np
from gym.spaces import Box, Dict, Discrete, MultiBinary, Tuple

from sr_gym.ipc.packet import GameState
from sr_gym.env.transformers.state_transformers import StateTransformer

class SimpleStateTransformer(StateTransformer):
    """
    The simplest state transformer, just returning the underlying state.
    """
    def __init__(self, num_players: int = 1):
        """
        Creates the state transformer for the number of players.

        Args:
            num_players: The number of players in the environment.
        """
        self._state_space: Dict = Dict({
            "info": Dict({
                "lap_time": Box(low=0, high=np.inf, shape=(1,))
            }),
            "players": Tuple(tuple(
                Dict({
                    "entity": Dict({
                        "position": Box(low=np.NINF, high=np.inf, shape=(2,)),
                        "velocity": Box(low=np.NINF, high=np.inf, shape=(2,)),
                        "grapple_radius": Box(low=0, high=np.inf, shape=(1,)),
                        "grapple_angle": Box(
                            low=-2 * np.pi, high=2 * np.pi, shape=(1,)
                        ),
                        "boost": Box(low=0, high=2, shape=(1,)),
                        "input": Dict({
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
                        }),
                        "in_air": MultiBinary(1),
                        "sliding": MultiBinary(1),
                        "sliding_on_ground": MultiBinary(1),
                        "grappling": MultiBinary(1),
                        "on_wall": MultiBinary(1),
                        "on_ground": MultiBinary(1),
                        "item": Discrete(20),
                        "last_move_direction": Box(low=-1, high=1, shape=(1,))
                    })
                })
                for _ in range(num_players)
            ))
        })

    def reset(self, initial_state: GameState) -> GameState:
        """
        Returns the initial state.

        Args:
            initial_state: The initial state of the environment to reset to.

        Returns:
            The initial state.
        """
        return initial_state

    def transform_state(self, state: GameState) -> GameState:
        """
        Returns the state.

        Args:
            state: The state to transform.
        
        Returns:
            The same input state.
        """
        return state

    def state_space(self) -> Dict:
        """
        The state space of the transformed state.

        Returns:
            The state space of the transformed state.
        """
        return self._state_space
