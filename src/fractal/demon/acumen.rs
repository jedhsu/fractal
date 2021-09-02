//! Acumen estimates the value of a position by simulating a random game
//! from it (a rollout).
//!
//!   + Puts a uniform prior on available actions.
//!   + Therefore, it can be used to implement the "vanilla" MCTS algorithm.

pub struct Acumen {
    nature: Nature,
    discount: f64,
    // RolloutOracle(gspec, γ=1.) = new{typeof(gspec)}(gspec, γ)
}

pub trait Interpret {
    fn appraise(&self, world: Realizing, decay: f64) -> f64;
    fn evaluate(&self);
}

impl Interpret for Acumen {
    fn appraise(world: Realizing, γ=1.) -> f64 {
        let reward = 0.;

        while !world.has_ended() {
            let action = world.possible_actions().random(); // TODO abstract this unform dist
            world.flow(action);

            reward = &self.discount * reward + world.white_reward();
        }

        reward
    }
    
    // TODO do tomrw
    fn evaluate (r::RolloutOracle)(state)
        game = GI.init(r.gspec, state)

        wp = GI.white_playing(g)
        n = length(GI.available_actions(g))
        P = ones(n) ./ n

        wr = rollout!(g, r.gamma)
        V = wp ? wr : -wr
        return P, V
}
