"""

    *Awaken*

  Return a report summarizing the configuration of agent before training starts,
  as an object of type [`Report.Initial`](@ref).

"""

from dataclasses import dataclass

from fractal.demon import Demon
from .._cognition import Cognition


@dataclass
class Awakened:
    number_parameters: int
    number_regularized_parameters: int
    demon: Demon
    memory_footprint_per_node: int


class Awaken(Cognition):
    def awakened(self):
        return Awakened(
            self.current_brain.number_parameters(),
            self.smartest_brain.number_regularized_parameters(),
            Demon(
                self.nature,
                self.current_brain,
                self.parameters.self_play.mcts,
            ),
        )
