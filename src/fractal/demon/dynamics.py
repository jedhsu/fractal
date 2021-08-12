from dataclasses import dataclass


@dataclass
class Dynamics:
    weights: int
    matrix: int
    action: int
    probability: int
    value: int
