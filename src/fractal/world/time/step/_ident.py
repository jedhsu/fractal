"""
Timestep Ident
==============

"""

from typing import Sequence


class TimestepIdent(
    tuple[int, ...],
):
    def __init__(
        self,
        ident: Sequence[int],
    ):
        super().__new__(
            tuple,
            ident,
        )
