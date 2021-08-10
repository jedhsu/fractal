"""

    *Bicameral Mind*

"""

from dataclasses import dataclass

from .._mind import Mind
from ..unicameral import UnicameralMind


@dataclass
class BicameralMind(Mind):
    white: UniCameralMind
    black: UnicameralMind
