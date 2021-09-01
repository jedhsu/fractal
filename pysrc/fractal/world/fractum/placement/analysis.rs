\\\!

    *Analysis*

  Analysis of a state.

\\\!

from datapub structes import datapub struct

from .placement import PlacementAnalysis
from .place import Place


@datapub struct
pub struct PlaceAnalysis(Place):
    distribution: set<PlacementAnalysis>
    expected_value: f64

    fn total(&self):
        return sum(s.N for s in b.stats)