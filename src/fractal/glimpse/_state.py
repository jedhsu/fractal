"""
Glimpsed World State
====================

"""

from dataclasses import dataclass

from ._action import GlimpsedAction


@dataclass
class GlimpsedWorldState:
    actions: set[GlimpsedAction]
    energy: float

    @property
    def num_visited(self) -> int:
        return sum(action.num_visited for action in self.actions)

    @classmethod
    def initialize(
        cls,
        prior_probability: float,
        energy: float,
        prior_temperature,
    ):
        P = Util.apply_temperature(
            prior_probability,
            prior_temperature,
        )
        glimpsed_actions = {GlimpsedAction(prior, 0, 0) for prior in P}
        return cls(glimpsed_actions, energy)
