from dataclasses import dataclass


@dataclass
class PlacementAnalysis(Placement):
    prior_probability: float  # Prior probability as given by the orac
    energy: float  # Cumulated Q-value for the action (Q = W/N)
    excites: int
