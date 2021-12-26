from sr_gym.ipc import Connection
from sr_gym.ipc.packet import PlayerInput
from sr_gym.env import SRGym
from sr_gym.env.transformers import TupleActionTransformer

if __name__ == "__main__":
    pipe_name = "\\\\.\\pipe\\SpeedRunners-dll"
    max_message_size = 1024

    #conn = Connection.create_named_pipe_connection(pipe_name, max_message_size)
    conn = None

    env = SRGym(conn, action_transformer=TupleActionTransformer())
    print(env.observation_space)
    print(env.action_space)

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
