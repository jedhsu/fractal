"""

    *Interpretation*

  Interpretation parameters.

"""

from dataclasses import dataclass

f64 = float


@dataclass
class DirichletNoise:
    epsilon: f64
    alpha: f64


@dataclass
class Interpretation:
    decay_factor: f64
    upper_confidence_threshold: f64
    noise: DirichletNoise
    previous_energy: f64


"""

  *Parameters:*

    * decay_factor: the reward discount factor
    * upper_confidence_threshold: exploration constant in the upper confidence threshold formula
    * noise: Dirichlet exploration [TODO] research
    * previous_energy: energy to apply to the oracle's output to get the prior probability vector used by MCTS.

"""
