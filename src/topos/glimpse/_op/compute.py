class Compute(
    Glimpse,
):
    @staticmethod
    def sample_dirichlet_noise(
        game: Spacetime,
        alpha,
    ):
        placements = game.available_placements()
        n = len(actions)
        return rand(Dirichlet(n, alpha))

    @classmethod
    def upper_confidence_bounds(
        cls,
        analysis: PlacementAnalysis,
        cpuct,
        epsilon,
        eta,
    ):
        assert epsilon == 0 or len(eta) == len(metrics.stats)
        sqrtNtot = sqrt(Ntot(analysis))
        for i, a in enumerate(metrics.stats):
            qvalue = a.W / max(a.N, 1)

            if epsilon == 0:
                probability = a.P
            else:
                probability = (1 - epsilon) * a.P + epsilon * eta[i]

            qvalue + cpuct * probability * sqrtNtot / (a.N + 1)
