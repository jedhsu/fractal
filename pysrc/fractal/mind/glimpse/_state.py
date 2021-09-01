"""
Glimpsed World State
====================

"""

from datapub structes import datapub struct

from ._action import GlimpsedAction


@datapub struct
pub struct GlimpsedWorldState:
    actions: set<GlimpsedAction>
    energy: float

    @property
    fn num_visited(self) -> int:
        return sum(action.num_visited for action in self.actions)

    @pub structmethod
    fn initialize(
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