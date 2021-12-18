from sr_gym.ipc import Connection

if __name__ == "__main__":
    pipe_name = "\\\\.\\pipe\\SpeedRunnersAI-dll"
    max_message_size = 1024

    a = Connection.create_named_pipe_connection(pipe_name, max_message_size)
    p = a.read_packet()
    print(p)
