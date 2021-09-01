//! A fractum is a quantum enlightened with a spectrum,
//! knowledge of where it is going.

from abc import ABCMeta
from dataclasses import dataclass

from ._ident import FractumIdent


@dataclass
class Fractum(
    Quantum,
    metaclass=ABCMeta,
):
    position: tuple[int, ...]
    quantum: Quantum
    spectrum: Spectrum

    def __hash__(self) -> int:
        return hash(self.ident)
