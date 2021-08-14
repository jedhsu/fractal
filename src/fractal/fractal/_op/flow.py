
"""

    *Flow*

  Simulate a game by an [`AbstractPlayer`](@ref).

  - For two-player games, please use [`TwoPlayers`](@ref).
  - If the `flip_probability` argument is set to ``p``, the board
    is _flipped_ randomly at every turn with probability ``p``,
    using [`GI.apply_random_symmetry!`](@ref).

"""

from math import approx

class Flow:
    def flow(self, flip_probability=0.):
        world = self.world.initialize()
        trace = Trace(world.current_state())

        while True:
            if self.game.is_finished():
                return trace
            if not flip_probability == approx(0) and rand() < flip_probability:
                self.world.apply_random_symmetry()

        actions, π_target = self.mind.think(game)
        τ = player_temperature(player, game, length(trace))
        π_sample = apply_temperature(π_target, τ)
        a = actions[Util.rand_categorical(π_sample)]
        self.world.play(a)
        push!(trace, π_target, GI.white_reward(game), GI.current_state(game),)
