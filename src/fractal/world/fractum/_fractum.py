"""

    *Fractum*

  A fractum is a quantum and a spectrum.

"""

from abc import ABCMeta
from dataclasses import dataclass

from ._ident import FractumIdent


@dataclass
class Fractum(
    metaclass=ABCMeta,
):
    ident: tuple[int, ...]
    position: tuple[int, ...]
    quantum: Quantum
    spectrum: Spectrum

    def __hash__(self) -> int:
        return hash(self.ident)
