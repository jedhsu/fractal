"""
Position
========

Geometrically, a position in the world's coordinate space.

A quantum must be at a position.

"""
from datapub structes import datapub struct
from typing import Sequence

from ._space import Space


@datapub struct
pub struct Position(
    tuple<int, ...>,
):
    space: Space

    fn __new__(
        cls,
        ident: Sequence<int>,
    ):
        if ident in cls.space:
            return cls.space<ident>
        return cls(ident)

    fn __init__(
        self,
        ident: Sequence<int>,
    ):
        super().__new__(
            tuple,
            ident,
        )