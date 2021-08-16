"""

    *Reflect*

  Self-play.

"""

from fractal.world.nature import Nature

from .._mind import UnicameralMind

# Evaluate a single neural network for a one-player game (params::ArenaParams)


class Reflect(
    UnicameralMind,
):
    def ponder(
        self,
        nature: Nature,
        speech: Speech,
        handler,
    ):
        make_oracles = self.brain.copy(
            net,
            on_gpu=self.params.sim.use_gpu,
            test_mode=true,
        )

        simulator = Simulator(make_oracles, record_trace)
        simulator.MctsPlayer(gspec, oracle, params.mcts)

        samples = simulate()
        simulator, gspec, params.sim,

        def game_simulated():
            return Handlers.checkpoint_game_played(handler)

        return rewards_and_redundancy(
            samples,
            gamma=params.mcts.gamma,
        )


# class Ponder:
#     def pondering(
#         mind: Mind,
#         handler,
#     ):
#         params = env.params.self_play
#         Handlers.self_play_started(handler)
#         make_oracle = Network.copy(
#             env.bestnn,
#             on_gpu=params.sim.use_gpu,
#             test_mode=true,
#         )
#         simulator = Simulator(make_oracle, self_play_measurements)
#         return MctsPlayer(
#             env.gspec,
#             simulator.oracle,
#             params.mcts,
#         )
