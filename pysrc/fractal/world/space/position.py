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
    tuple<i32, ...>,
):
    space: Space

    fn __new__(
        cls,
        ident: Sequence<i32>,
    ):
        if ident in cls.space:
            return cls.space<ident>
        return cls(ident)

    fn __init__(
        self,
        ident: Sequence<i32>,
    ):
        super().__new__(
            tuple,
            ident,
        )