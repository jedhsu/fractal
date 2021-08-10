"""

    *Energy*

  Return the energy of the mind, given the number of actions that have
  been played before by both players in the current game.

  A default implementation is provided that always returns 1.

"""

from .._demon import Demon


class Energy(
    Mind,
):
    def energy(
        self,
        topos: Topos,
        epoch: int,
    ) -> float:
        return 1.0
