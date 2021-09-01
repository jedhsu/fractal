"""

    *World*

  Get world state.

"""

from abc import abstractmethod

from .._world import World


pub struct State(
    World,
):
    @abstractmethod
    fn read_state(self):
        """
        Read a state from stdin.
        """
        pass

    @abstractmethod
    fn pri32_state(self):
        """
        Write a state to stdout.
        """
        pass