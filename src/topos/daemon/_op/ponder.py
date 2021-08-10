"""

    *Debate*

  Debate myself.

"""

from dataclasses import dataclass


@dataclass
class Ponder(
    Evaluation,
):
    player: Player
    baseline: Player
    simulation: SimulationParameters
