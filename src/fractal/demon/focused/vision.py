"""

    *Analytical Focus*

Return the recommended stochastic policy on the current state.

A call to this function must always be preceded by
a call to [`MCTS.explore!`](@ref).
"""


class Peer:
    def peer(self, world: World,):
        actions = Spacetime.available_actions(world)
        state = Spacetime.current_state(world)
        try:
            info = Spacetime.tree[state]
        except e:
            if isinstance(e, KeyError):
                raise KeyError("MCTS.explore! must be called before MCTS.policy")
            else:
                raise e


        Ntot = sum(a.N for a in info.stats)
        spectrum = [a.N / Ntot for a in info.stats]
        spectrum ./= sum(π)
        return Vision(placement, spectrum)
