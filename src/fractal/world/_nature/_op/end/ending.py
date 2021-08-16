"""
World Ended
=========

A way in which the world terminates.

"""

from typing import Callable
from dataclasses import dataclass


@dataclass
class WorldEnded(World):
    name: str
    condition: Callable[..., bool]
    end_state: EndState

    def states(self):
        pass


def tictactoe_no_more_spaces(self):
    return all(block.state == TicTacToe_Block.Empty for block in self.blocks)


def tictactoe_white_won(self):
    return any(self.three_in_a_row().all_white())


def tictactoe_black_won(self):
    return any(self.three_in_a_row().all_black())


TicTacToe_Full = WorldEnded("No more spaces.", TicTacToe_EndState.Draw)
