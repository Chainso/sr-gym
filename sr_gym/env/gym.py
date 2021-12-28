from typing import Any, Dict, Tuple

from gym import Env

from sr_gym.ipc import Connection
from sr_gym.env.transformers import (
    StateTransformer, SimpleStateTransformer, ActionTransformer,
    SimpleActionTransformer, RewardTransformer, VelocityRewardTransformer,
    TerminalTransformer, LapTerminalTransformer
)

class SRGym(Env):
    """
    A gym environment for SpeedRunners.
    """
    def __init__(
            self,
            connection: Connection,
            state_transformer: StateTransformer = SimpleStateTransformer(),
            action_transformer: ActionTransformer = SimpleActionTransformer(),
            reward_transformer: RewardTransformer = VelocityRewardTransformer(),
            terminal_transformer: TerminalTransformer = LapTerminalTransformer()
        ):
        """
        Creates the gym environment using an existing connection.

        Args:
            connection: The connection to get packets from.
            state_transformer: The transformer to transform states.
            action_transformer: The transformer to transform input actions.
            reward_transformer: The transformer to calculate rewards with.
            terminal_transformer: The transformer to determine terminals with.
        """
        super().__init__()

        self.connection = connection
        self.state_transformer = state_transformer
        self.action_transformer = action_transformer
        self.reward_transformer = reward_transformer
        self.terminal_transformer = terminal_transformer

        self.observation_space = self.state_transformer.state_space()
        self.action_space = self.action_transformer.action_space()

        # Store the current state
        self.state = None

    def reset(self) -> Any:
        """
        Resets the SpeedRunners game and current lap.

        Returns:
            The initial state of the environment.
        """
        initial_state = self.connection.read_packet()
        self.state = initial_state

        transformed_initial_state = self.state_transformer.reset(initial_state)

        self.action_transformer.reset(initial_state)
        self.reward_transformer.reset(initial_state)
        self.terminal_transformer.reset(initial_state)

        return transformed_initial_state

    def step(self, action: Any) -> Tuple[Any, float, bool, Dict]:
        """
        Takes one step in the SpeedRunners game, executing the action.

        Args:
            action: The action to execute.

        Returns:
            A tuple of (next state, reward, terminal, info).
        """
        info = {}

        parsed_act = self.action_transformer.transform_action(action)
        self.connection.send_packet(parsed_act.to_json())
        
        next_state = self.connection.read_packet()
        transformed_next_state = self.state_transformer.transform_state(
            next_state
        )

        terminal = self.terminal_transformer.transform_terminal(
            self.state, parsed_act, next_state, info
        )

        reward = self.reward_transformer.transform_reward(
            self.state, parsed_act, next_state, terminal
        )

        self.state = next_state

        return transformed_next_state, reward, terminal, info

    def render(self) -> None:
        """
        Renders the environment.
        """
        # Environment is rendered by default, nothing to be done
        return

    def close(self) -> None:
        """
        Closes the gym environment.
        """
        self.connection.close()
