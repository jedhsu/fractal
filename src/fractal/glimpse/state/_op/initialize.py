from math import approx


class Initialize(State):
    @classmethod
    def initialize(
        cls,
        probability,
        value,
        prior_temperature,
    ):
        P = Util.apply_temperature(P, prior_temperature)
        stats = [PlacementAnalysis(p, 0, 0) for p in P]
        return StateInfo(stats, V)
