"""

    *Step Ident*

"""

from typing import Sequence


class StepIdent(tuple[int, ...]):
    def __init__(
        self,
        ident: Sequence[int],
    ):
        super().__new__(
            tuple,
            ident,
        )
