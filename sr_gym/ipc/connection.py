from __future__ import annotations

import win32file
import win32pipe

from sr_gym.ipc.packet import GameState

class Connection:
    """
    A connection to a pipe providing I/O for SpeedRunners.
    """
    def __init__(self, pipe: win32file.PyHandle, max_message_size: int):
        """
        Creates a connection to the I/O pipe for SpeedRunners

        Args:
            pipe: The pipe to send and receive messages from.
            max_message_size: The maximum message size to read from the pipe.
        """
        self.pipe = pipe
        self.max_message_size = max_message_size

    @staticmethod
    def create_named_pipe_connection(
        pipe_name: str,
        max_message_size: int
    ) -> Connection:
        """
        Creates a connection using a named pipe.

        Args:
            pipe_name: The name of the pipe to open.
            max_message_size: The maximum message size to read from the pipe.

        Returns:
            A connection using the newly opened named pipe.
        """
        pipe = win32file.CreateFile(
            pipe_name, win32file.GENERIC_READ | win32file.GENERIC_WRITE,
            0, None, win32file.OPEN_EXISTING, 0, None
        )
        pipe_state_set = win32pipe.SetNamedPipeHandleState(
            pipe, win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT, None,
            None
        )

        if pipe_state_set == 0:
            # Failed to set pipe mode, TODO: error handling
            pass

        return Connection(pipe, max_message_size)

    def read_packet(self) -> GameState:
        """
        Reads a single packet from the pipe.

        Returns:
            The packet read as a game dataclass.
        """
        _, message = win32file.ReadFile(self.pipe, self.max_message_size)

        if message is None:
            # Problem reading, TODO: error handling
            pass

        print("Read:", message)
        return GameState.from_json(message)

    def send_packet(self, message: bytes) -> None:
        """
        Sends a packet through the pipe.

        Args:
            message: The message to send through the pipe.
        """
        win32file.WriteFile(self.pipe, message)

    def close(self) -> None:
        """
        Closes the connection.
        """
        self.pipe.close()
