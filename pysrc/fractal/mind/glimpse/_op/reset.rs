\\\!
Glimpsing - Reset
=================

Empty the MCTS tree.

\\\!

from ..glimpsing import Glimpsing


pub struct Reset(
    Glimpsing,
):
    fn reset(&self):
        &self.tree = dict()