//! Ignorance randomly selects actions with equal probability.

// pub trait Ignorance: Demon {
// }
//     pass

pub trait Ignorance: Demon {
    fn temperature(&self, world: &Realizing) -> Temperature;
    fn think(&self, world: &Realizing) -> Action;
}


impl Display for Ignorance {
    // # name(p::MinMaxTS) = "MinMax (depth $(p.depth))"
}

impl Ignorance for Demon {
    fn new(
        nature: Nature,
    ) {
        // TODO clean this up from glimpse paramers
        gamma = 1.0
        cpuct = 1.0
        noise_ϵ = 0.0
        noise_α = 1.0
        prior_temperature = 1.0

        S = Time.state_type(physics)
        tree: dict<S, StateInfo> = dict()
        total_simulations = 0
        total_nodes_traversed = 0

        Ignorance {
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
        }
}
    fn temperature(&self, realizing: Realizing) {};
    fn think(&self, realizing: Realizing) {
        let actions = realizing.possible_actions();
        let n = actions.len();
        let spectrum = n.ones() / actions.len();

        Place(actions, spectrum)
    }
}
