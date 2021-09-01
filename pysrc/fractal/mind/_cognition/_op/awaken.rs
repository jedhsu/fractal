"""

    *Awaken*

  Return a report summarizing the configuration of agent before training starts,
  as an object of type <`Report.Initial`>(@ref).

"""

from datapub structes import datapub struct

from fractal.demon import Demon
from .._cognition import Cognition


@datapub struct
pub struct Awakened:
    number_parameters: i32
    number_regularized_parameters: i32
    demon: Demon
    memory_footpri32_per_node: i32


pub struct Awaken(Cognition):
    fn awakened(self):
        return Awakened(
            self.current_brain.number_parameters(),
            self.smartest_brain.number_regularized_parameters(),
            Demon(
                self.nature,
                self.current_brain,
                self.parameters.self_play.mcts,
            ),
        )