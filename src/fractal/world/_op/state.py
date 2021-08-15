"""

    *World*

  Get world state.

"""

from .._world import World


class State(
    World,
):
    def read_state(self):
        """
        Read a state from stdin.
        """

    def write_state(self):
        """
        Write a state to stdout.
        """
        pass
