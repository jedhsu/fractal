"""
Glimpsed Action
===============

"""

from dataclasses import dataclass


@dataclass
class GlimpsedAction:
    prior_probability: float
    energy: float
    num_visited: int
