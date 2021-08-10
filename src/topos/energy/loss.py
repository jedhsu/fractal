from dataclasses import dataclass


@dataclass
class Loss:
    total: float
    cross_entropy: float
    average_mse: float
    regularization: float
    invalid: float
