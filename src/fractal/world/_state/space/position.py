"""
Position
========

Geometrically, the position of a quantum in the world's coordinate space.

"""
from dataclasses import dataclass
from typing import Sequence

from ._space import Space


@dataclass
class Position(
    tuple[int, ...],
):
    space: Space

    def __new__(
        cls,
        ident: Sequence[int],
    ):
        if ident in cls.space:
            return cls.space[ident]
        return cls(ident)

    def __init__(
        self,
        ident: Sequence[int],
    ):
        super().__new__(
            tuple,
            ident,
        )
