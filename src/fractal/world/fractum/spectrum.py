"""

    *Spectrum*

  A probability distribution of quantum placements.

"""

from abc import ABCMeta
from typing import Mapping

from .quantum import Quantum


class Spectrum(
    Simplex[Cube, Globe],
    Mapping[float, Quantum],
    metaclass=ABCMeta,
):
    pass
