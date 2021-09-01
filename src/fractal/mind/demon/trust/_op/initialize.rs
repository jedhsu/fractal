\\\!

    *Emerge*

\\\!


pub struct Emerge(
    FocusedDemon,
):
    fn emerge(
        &self,
        physics: Physics,
    ):
        gamma = 1.0
        cpuct = 1.0
        noise_ϵ = 0.0
        noise_α = 1.0
        prior_temperature = 1.0

        S = Time.state_type(physics)
        tree: dict<S, StateInfo> = dict()
        total_simulations = 0
        total_nodes_traversed = 0

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