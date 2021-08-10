"""

    *Duel*

  Run a benchmark duel and return a [`Report.Evaluation`](@ref).

"""

from .._daemon import Daemon


class Duel(Daemon):
    def battling(
        topos: Topos,
        view: View,
        progress=None,
    ):
        net() = Network.copy(topos.bestnn, on_gpu=eval.sim.use_gpu, test_mode=true,)
        # if isinstance(eval, Single):
        #     simulator = Simulator(net, record_trace)
        #     simulator.instantiate(eval.player, env.gspec, net)
        # else:
        #     assert isinstance(eval, Battle)
        #     simulator = Simulator(net, record_trace)
        #     simulator.instantiate(eval.player, env.gspec, net)
        #     baseline = instantiate(eval.baseline, env.gspec, net)
        #     return Dual(player, baseline)

        #   samples, elapsed = @timed simulate(
        #     simulator, env.gspec, eval.sim,

    def simulate():
        def simulating():
            return next(progress)
        return simulating

        gamma = world.nature.ponder.mcts.gamma
        rewards, redundancy = rewards_and_redundancy(samples, gamma=gamma)
    # return Report.Evaluation(
      #   name(eval),
      #   mean(rewards),
      #   redundancy,
      #   rewards,
      #   nothing,
      #   elapsed,
    # )


"""
If a `progress` is provided, `next!(progress)` is called
after each simulated game.
"""
