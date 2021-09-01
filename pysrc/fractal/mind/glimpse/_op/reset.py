"""
Glimpsing - Reset
=================

Empty the MCTS tree.

"""

from ..glimpsing import Glimpsing


class Reset(
    Glimpsing,
):
    def reset(self):
        self.tree = dict()
