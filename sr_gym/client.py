from time import sleep

from sr_gym.ipc import Connection, MAX_MESSAGE_SIZE
from sr_gym.ipc.packet import PlayerInput

if __name__ == "__main__":
    pipe_name = "\\\\.\\pipe\\SpeedRunners-dll"

    conn = Connection.create_named_pipe_connection(pipe_name, MAX_MESSAGE_SIZE)

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

    conn.close()
