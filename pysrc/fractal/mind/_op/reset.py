"""

    *Go*

  Reset the internal memory of a player (e.g. the MCTS tree).
  The default implementation does nothing.

"""

from .._demon import Demon


class Go(
    Demon,
):
    def reincarnate(self):
        pass
