"""
Optimized
=========

Loss metrics.

"""


from dataclasses import dataclass


@dataclass
class Optimized:
    total: float
    cross_entropy: float
    average_mse: float
    regularization: float
    invalid: float
