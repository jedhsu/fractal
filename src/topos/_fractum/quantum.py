"""

    *Quantum*

  A quantum is a globe.

  The integer is its ideal.

"""

from abc import ABCMeta
from typing import Hashable


class Quantum(
    Globe[Simplex[Cube, Cube]],
    Hashable,
    metaclass=ABCMeta,
):
    pass
