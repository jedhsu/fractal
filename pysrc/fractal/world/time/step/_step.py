"""

    *Timestep*

  An atomic unit of time.

"""

from dataclasses import dataclass

from typing import Hashable
from ._ident import TimestepIdent


@dataclass
class Timestep(
    Hashable,
):
    ident: TimestepIdent

    def __hash__(self):
        return hash(
            (
                self.__class__,
                self.ident,
            )
        )
