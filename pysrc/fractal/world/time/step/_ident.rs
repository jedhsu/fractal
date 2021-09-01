\\\!
Timestep Ident
==============

\\\!

from typing import Sequence


pub struct TimestepIdent(
    tuple<i32, ...>,
):
    fn __init__(
        &self,
        ident: Sequence<i32>,
    ):
        super().__new__(
            tuple,
            ident,
        )