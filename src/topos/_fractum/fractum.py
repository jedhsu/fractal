"""

    *Fractum*

  A fractum is a quantum and a spectrum.

"""

from abc import ABCMeta

from .quantum import Quantum
from ._simplex import Simplex


class Fractum(
    Simplex[Quantum, Spectrum],
    metaclass=ABCMeta,
):
    pass
