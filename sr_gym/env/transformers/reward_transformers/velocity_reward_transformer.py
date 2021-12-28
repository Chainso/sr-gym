import numpy as np

from sr_gym.ipc.packet import GameState, PlayerInput
from sr_gym.env.transformers.reward_transformers import RewardTransformer

class VelocityRewardTransformer(RewardTransformer):
    """
    Calculates a reward based on the velocity of the player.
    """
    def reset(self, initial_state: GameState) -> None:
        """
        Resets the reward transformer using the initial state, effectively doing
        nothing.

        Args:
            initial_state: The initial state of the environment to reset to.
        """   
        # Nothing needs to be done
        return

    def transform_reward(
            self,
            state: GameState,
            action: PlayerInput,
            next_state: GameState,
            terminal: bool
        ) -> float:
        """
        Transforms a single reward based on the velocity of the new state.

        Args:
            state: The state before the action was taken.
            action: The action that was taken.
            next_state: The state after the action was taken.
            terminal: If the new state is a terminal state.
        
        Returns:
            The calculated reward.
        """
        velocity = next_state.players[0].entity.velocity
        reward = np.linalg.norm([velocity.x / 500, velocity.y / 1000])

        return reward
