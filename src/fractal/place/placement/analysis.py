@dataclass
class PlacementAnalysis:
    vec: Vector[ActionStats]
    expected_value: float  # Value estimate given by the oracle

    def total(self):
        return sum(s.N for s in b.stats)
