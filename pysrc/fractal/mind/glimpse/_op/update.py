"""
Glimpsing - Update
=================

"""

from ..glimpsing import Glimpsing

from fractal.world import WorldState


pub struct Update(
    Glimpsing,
):
    fn update_world_state(
        self,
        worldstate: WorldState,
        action: Action,
        energy: Energy,
    ):
        stats = worldstate.tree<state>.stats
        astats = stats<action_id>
        stats<action_id> = PlacementAnalysis(
            astats.P,
            astats.W + q,
            astats.N + 1,
        )