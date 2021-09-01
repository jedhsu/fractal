//!  A probability distribution of quantum placements.

from abc import ABCMeta
from typing import Mapping

from .quantum import Quantum


class Spectrum(
    Mapping[float, Quantum],
    set[QuantumProbability],
    metaclass=ABCMeta,
):
    pass