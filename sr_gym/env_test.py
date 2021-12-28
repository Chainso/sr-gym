from time import time

import orjson
import numpy as np

from sr_gym.ipc import Connection
from sr_gym.ipc.packet import GameState, PlayerInput
from sr_gym.env import SRGym
from sr_gym.env.transformers import (
    TupleStateTransformer, TupleActionTransformer, DiscreteActionTransformer,
    VelocityRewardTransformer, LapTerminalTransformer
)

if __name__ == "__main__":
    pipe_name = "\\\\.\\pipe\\SpeedRunners-dll"
    max_message_size = 1024

    conn = Connection.create_named_pipe_connection(pipe_name, max_message_size)
    #conn = None

    env = SRGym(
        conn,
        state_transformer=TupleStateTransformer(),
        action_transformer=DiscreteActionTransformer(),
        reward_transformer=VelocityRewardTransformer(),
        terminal_transformer=LapTerminalTransformer()
    )
    print(env.observation_space)
    print(env.action_space)
    print()

    print(env.observation_space.shape, np.prod(env.observation_space.shape))
    print(env.action_space.shape, np.prod(env.action_space.shape))

    num_obs = np.sum(np.prod(env.observation_space.shape, axis=-1))
    num_acts = np.sum(env.action_space.shape)

    print(num_obs)
    print(num_acts)

    print(env.action_space.sample())

    length = 30
    acts = 0

    
    start = time()

    print("Reset to packet:", env.reset())
    while time() - start < length:
        action = env.action_space.sample()
        print(action)

        acts += 1
        ns, reward, terminal, info = env.step(action)
        print(reward, terminal, info)

    acts_per_sec = acts / length

    print("APS:", acts_per_sec)

    """
    counts = 1

    for _ in range(counts):
        packet = conn.read_packet()
        print(packet)

        conn.send_packet(inputs.to_json())

        print("Sending: " + inputs.to_json().decode("utf-8"))

        inputs.left = not inputs.left
        inputs.right = not inputs.right
        inputs.jump = not inputs.jump
    """
    conn.close()
