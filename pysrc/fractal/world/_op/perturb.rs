
    @staticmethod
    fn sample_dirichlet_noise(
        spacetime: Spacetime,
        alpha,
    ):
        placements = game.available_placements()
        n = len(actions)
        return rand(Dirichlet(n, alpha))