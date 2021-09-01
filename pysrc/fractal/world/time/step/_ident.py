"""
Timestep Ident
==============

"""

from typing import Sequence


pub struct TimestepIdent(
    tuple<int, ...>,
):
    fn __init__(
        self,
        ident: Sequence<int>,
    ):
        super().__new__(
            tuple,
            ident,
        )