"""
Space
=====

Geometrically, the space defined by the world.

"""

from dataclasses import dataclass

from tensor import Tensor

from typing import Collection
from typing import Mapping
from typing import Sequence

from ..fractum.quantum import Position

from itertools import product


class Placement(
    tuple[int, ...],
):
    pass


@dataclass
class Space(
    Tensor,
    Mapping[tuple[int, ...], Position],
    Collection[Position],
):
    positions: set[Position]

    def __len__(self) -> int:
        return len(self.positions)

    def __getitem__(
        self,
        position: Sequence[int],
    ) -> Position:
        return Position(position)


class Test:
    class TicTacToe_Space(
        Space,
    ):
        def construct(self):
            return super().construct(
                product(
                    [1, 2, 3],
                    [1, 2, 3],
                )
            )
