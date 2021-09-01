"""

    *Reflect*

  Self-play.

"""

from fractal.world.nature import Nature

from .._mind import UnicameralMind

# Evaluate a single neural network for a one-player game (params::ArenaParams)


pub struct Reflect(
    UnicameralMind,
):
    fn reflect(
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

        fn game_simulated():
            return Handlers.checkpoi32_game_played(handler)

        return rewards_and_redundancy(
            samples,
            gamma=params.mcts.gamma,
        )


# pub struct Ponder:
#     fn pondering(
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