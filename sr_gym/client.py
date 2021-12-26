from time import sleep

from sr_gym.ipc import Connection
from sr_gym.ipc.packet import PlayerInput

if __name__ == "__main__":
    pipe_name = "\\\\.\\pipe\\SpeedRunners-dll"
    max_message_size = 1024

    conn = Connection.create_named_pipe_connection(pipe_name, max_message_size)

    inputs = PlayerInput(
        left=True,
        right=False,
        jump=False,
        grapple=True,
        weapon=False,
        item=False,
        taunt=False,
        swap_weapon=False,
        slide=False,
        boost=False
    )

    counts = 10

    for _ in range(counts):
        packet = conn.read_packet()
        print(packet)

        print("Sending: " + inputs.to_json())
        conn.send_packet(inputs.to_json())

        inputs.left = not inputs.left
        inputs.right = not inputs.right
        inputs.jump = not inputs.jump

        sleep(1)

    conn.close()
