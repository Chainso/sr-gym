from typing import Any

from gym.spaces import Discrete

class DiscreteShaped(Discrete):
    """
    A discrete space, with the shape being a 1-D tuple of 1 value.
    """
    def __init__(self, *args: Any, **kwargs: Any):
        """
        Creates the discrete space with the shape attribute.

        Args:
            args: Arguments for the underlying discrete shape.
            kwargs: Keyword arguments for the underlying discrete shape.
        """
        super().__init__(*args, **kwargs)

        self._shape = (1,)

class OneHotDiscreteShaped(Discrete):
    """
    A discrete space, where the shape is a 1-D tuple of number of values the
    discrete distribution can take on.
    """
    def __init__(self, *args: Any, **kwargs: Any):
        """
        Creates the discrete space with the shape attribute.

        Args:
            args: Arguments for the underlying discrete shape.
            kwargs: Keyword arguments for the underlying discrete shape.
        """
        super().__init__(*args, **kwargs)

        self._shape = (self.n,)
