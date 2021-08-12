"""

    *Spectrum*

  A distribution of quantums.

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
