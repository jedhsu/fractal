"""
Glimpse
=======

Parameters for MCTS.

"""

f64 = float

from dataclasses import dataclass


@dataclass
class Glimpse(
    Demon,
):
    # Parameters
    decay: f64  # Discount factor
    cpuct: f64
    epsilon_noise: f64
    alpha_noise: f64
    prior_health: f64
