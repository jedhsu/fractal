"""

    *Health*

  Return the health of the mind, given the number of actions that have
  been played before by both players in the current game.

  A default implementation is provided that always returns 1.

"""

from .._mind import Mind


class Health(
    Mind,
):
    def health(
        self,
        timestep: Timestep,
    ) -> float:
        return 1.0
