"""

    *Analysis*

  Analysis of a state.

"""

from dataclasses import dataclass

from .placement import PlacementAnalysis
from .place import Place


@dataclass
class PlaceAnalysis(Place):
    distribution: set[PlacementAnalysis]
    expected_value: float

    def total(self):
        return sum(s.N for s in b.stats)
