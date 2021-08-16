"""

    *Evolved*

"""

from dataclasses import dataclass

from .optimized import Optimized


@dataclass
class Evolved(
    Optimized,
):
    demon_entropy: float
    brain_entropy: float


def evolution_status(
    tr: Trainer,
    samples,
):
