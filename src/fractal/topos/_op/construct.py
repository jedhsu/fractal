class Construct(
    Topos,
):
    @classmethod
    def construct(
        gspec,
        oracle,
        gamma=1.0,
        cpuct=1.0,
        noise_ϵ=0.0,
        noise_α=1.0,
        prior_temperature=1.0,
    ):
        nature = physics.nature()
        tree: Dict[S, StateInfo] = dict()

    nglimpses = 0
    ntraversals = 0

    return cls(
        tree,
        oracle,
        gamma,
        cpuct,
        noise_ϵ,
        noise_α,
        prior_temperature,
        total_simulations,
        total_nodes_traversed,
        gspec,
    )
