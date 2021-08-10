"""

    *Energy*

  Return the player temperature, given the number of actions that have
  been played before by both players in the current game.

  A default implementation is provided that always returns 1.

"""

from .._demon import Demon


class Energy(
    Demon,
):
    def energy(
        self,
        topos: Topos,
        epoch: int,
    ) -> float:
        return 1.0
