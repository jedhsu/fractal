"""
Thinking, [Think]
=================

Add a new (policy, reward, state) quadruple.

"""

from .._thinking import Thinking


class Think(
    Thinking,
):
    def think(
        self,
        state: WorldState,
        daemon: Daemon,
        energy: Energy,
    ):
        pass

    def _validate(self):
        pass
