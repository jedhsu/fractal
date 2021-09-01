\\\!
World Place

===========

A macroscopic configuration.

Contains set of states.

Ultimate goal is to allow this to be parametrizable by algo.

\\\!

from abc import ABCMeta

from typing import Iterator


pub struct WorldPlace(
    World,
    Iterator<WorldPosition>,
    metapub struct=ABCMeta,
):
    pass


pub struct TicTacToe_ThreeConsecutiveWhites:
    pass