"""
World Place

===========

A macroscopic configuration.

Contains set of states.

Ultimate goal is to allow this to be parametrizable by algo.

"""

from abc import ABCMeta

from typing import Iterator


class WorldPlace(
    World,
    Iterator[WorldPosition],
    metaclass=ABCMeta,
):
    pass


class TicTacToe_ThreeConsecutiveWhites:
    pass
