import numpy as np

from sr_gym.ipc import Connection
from sr_gym.ipc.packet import PlayerInput
from sr_gym.env import SRGym
from sr_gym.env.transformers import (
    TupleStateTransformer, TupleActionTransformer
)

if __name__ == "__main__":
    pipe_name = "\\\\.\\pipe\\SpeedRunners-dll"
    max_message_size = 1024

    #conn = Connection.create_named_pipe_connection(pipe_name, max_message_size)
    conn = None

    env = SRGym(
        conn,
        state_transformer=TupleStateTransformer(),
        action_transformer=TupleActionTransformer()
    )
    print(env.observation_space)
    print(env.action_space)
    print()

    print(env.observation_space.shape, np.prod(env.observation_space.shape))
    print(env.action_space.shape, np.prod(env.action_space.shape))

    num_obs = np.sum(np.prod(env.observation_space.shape, axis=-1))
    num_acts = np.sum(np.prod(env.action_space.shape, axis=-1))

    print(num_obs)
    print(num_acts)
    """
    inputs = PlayerInput(
        left=True,
        right=False,
        jump=False,
        grapple=False,
        weapon=False,
        item=False,
        taunt=False,
        swap_weapon=False,
        slide=False,
        boost=False
    )

    counts = 1000

    for _ in range(counts):
        packet = conn.read_packet()
        print(packet)

        print("Sending: " + inputs.to_json())
        conn.send_packet(inputs.to_json())

        inputs.left = not inputs.left
        inputs.right = not inputs.right
        inputs.jump = not inputs.jump

    #conn.close()
    """
