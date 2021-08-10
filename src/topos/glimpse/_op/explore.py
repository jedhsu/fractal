"""

    MCTS.explore!(env, game, nsims)

  Run `nsims` MCTS simulations from the current state.

"""

class Explore(Glimpse):
    @staticmethod
    def explore(vision: Vision, game, number_of_glimpses: int):
        η = dirichlet_noise(game, topos.noise_α)
        for i in range(1, nsims):
            vision.total_simulations += 1
            run_simulation!(env, GI.clone(game), η=η)
