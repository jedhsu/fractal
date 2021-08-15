"""

    *Gauge*

  Evaluating by pitting it against a baseline player in a two-player game.

"""

from dataclasses import dataclass

from .._demon import Demon


@dataclass
class Gauge(Demon):
    baseline: Player
    simulation: SimulationParameters
