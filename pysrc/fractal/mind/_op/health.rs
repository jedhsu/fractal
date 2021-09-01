"""

    *Health*

  Return the health of the mind, given the number of actions that have
  been played before by both players in the current game.

  A fnault implementation is provided that always returns 1.

"""

from .._mind import Mind


pub struct Health(
    Mind,
):
    fn health(
        self,
        timestep: Timestep,
    ) -> f64:
        return 1.0