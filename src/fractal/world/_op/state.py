"""

    *World*

  Get world state.

"""

from abc import abstractmethod

from .._world import World


class State(
    World,
):
    @abstractmethod
    def read_state(self):
        """
        Read a state from stdin.
        """
        pass

    @abstractmethod
    def print_state(self):
        """
        Write a state to stdout.
        """
        pass
