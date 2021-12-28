# With some credits to https://github.com/lucas-emery/rocket-league-gym/blob/main/rlgym/utils/reward_functions/combined_reward.py
from __future__ import annotations
from typing import Optional, Tuple, Union

import numpy as np

from sr_gym.ipc.packet import GameState, PlayerInput
from sr_gym.env.transformers.reward_transformers import RewardTransformer

class CombinedRewardTransformer(RewardTransformer):
    """
    Combines multiple reward transformers into a single reward.
    """
    def __init__(
            self,
            reward_transformers: Tuple[RewardTransformer, ...],
            reward_weights: Optional[Tuple[float, ...]] = None
        ):
        """
        Creates the combined reward transformer using the reward transformers
        given and the weights given for each reward.

        Args:
            reward_transformers: The reward transformers to combine.
            reward_weights: The weights for each reward, or None for uniform
                weighting.
        """
        super().__init__()

        self.reward_transformers = reward_transformers
        self.reward_weights = (
            reward_weights or np.ones_like(reward_transformers)
        )

        if len(self.reward_transformers) != len(self.reward_weights):
            raise ValueError(
                "The number of reward transformers ({0}) and weights ({1}) " \
                "must be equal".format(
                    len(self.reward_functions), len(self.reward_weights)
                )
            )

    @classmethod
    def from_zipped(
            cls: CombinedRewardTransformer,
            *rewards_and_weights: Union[RewardTransformer,
                                        Tuple[RewardTransformer, float]]
        ) -> CombinedRewardTransformer:
        """
        Creates the combined reward transformer using tuples of reward
        reward transformers and weights. Reward transformers on their own have
        a weight of 1 by default.

        Args:
            cls: The combined reward transformer class to create.
            rewards_and_weights: A sequence of reward transformer and weight
                tuples or reward transformers on their own.

        Returns:
            The combined reward transformer from the given transformers and
            weights.
        """
        rewards = []
        weights = []

        for value in rewards_and_weights:
            if isinstance(value, tuple):
                reward_transformer, weight = value
            else:
                reward_transformer, weight = value, 1.

            rewards.append(reward_transformer)
            weights.append(weight)

        return cls(tuple(rewards), tuple(weights))

    def reset(self, initial_state: GameState) -> None:
        """
        Resets all of the underlying reward transformers.

        Args:
            initial_state: The initial state the environment is being reset to.
        """ 
        for reward_transformer in self.reward_transformers:
            reward_transformer.reset(initial_state)

    def transform_reward(
            self,
            state: GameState,
            action: PlayerInput,
            next_state: GameState,
            terminal: bool
        ) -> float:
        """
        Transforms a single reward into the weighted total of all the rewards.

        Args:
            state: The state before the action was taken.
            action: The action that was taken.
            next_state: The state after the action was taken.
            terminal: If the new state is a terminal state.
        
        Returns:
            The combined rewards.
        """
        rewards = [
            reward_transformer.transform_reward(
                state, action, next_state, terminal
            )
            for reward_transformer in self.reward_transformers
        ]

        return float(np.dot(self.reward_weights, rewards))
