"""
Fractum Ident
=============

"""

from typing import Sequence


class FractumIdent(
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
