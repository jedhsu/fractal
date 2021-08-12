"""

    *Quantum*

  A quantum is a globe.

  The integer is its ideal.

"""

from abc import ABCMeta
from typing import Hashable

from ._globe import Globe
from ._simplex import Simplex
from ._cube import Cube


class Quantum(
    Globe[Simplex[Cube, Cube]],
    Hashable,
    metaclass=ABCMeta,
):
    pass
