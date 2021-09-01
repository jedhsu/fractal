"""
Glimpsing - Compute
===================

"""

from ..glimpsing import Glimpsing

from math import sqrt

from .._state import GlimpsedWorldState


class Compute(
    Glimpsing,
):
    @staticmethod
    def upper_confidence_bounds(
        glimpsed_state: GlimpsedWorldState,
        cpuct,
        epsilon,
        eta,
    ):
        assert epsilon == 0 or len(eta) == len(glimpsed_state.actions)
        sqrt_num_visited = sqrt(glimpsed_state.num_visited)
        for i, action in enumerate(glimpsed_state.actions):
            qvalue = action.energy / max(action.num_visited, 1)

            if epsilon == 0:
                probability = action.prior_probability
            else:
                # [TODO] clean me functionally
                probability = (1 - epsilon) * action.prior_probability + epsilon * eta[
                    i
                ]

            qvalue + cpuct * probability * sqrt_num_visited / (a.N + 1)

    def depth_of_analysis(self) -> float:
        """
        Return the average number of nodes that are traversed during an
        MCTS simulation, not counting the root.
        """
        if self.total_simulations == 0:
            return 0
        return self.total_nodes_traversed / self.total_simulations
