\\\!
Thinking, <Think>
=================

Add a new (policy, reward, state) quadruple.

\\\!

from .._thinking import Thinking


pub struct Think(
    Thinking,
):
    fn think(
        &self,
        state: WorldState,
        daemon: Daemon,
        energy: Energy,
    ):
        pass

    fn _validate(&self):
        pass