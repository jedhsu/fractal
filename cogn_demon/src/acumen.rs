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

            let reward = &self.discount * reward + world.white_reward();
        }

        reward
    }
    
    fn evaluate(r::RolloutOracle)(state) {
        game = GI.init(r.gspec, state)

        let wp = GI.white_playing(g);
        let n = length(GI.available_actions(g));
        let P = ones(n) ./ n;

        let wr = rollout!(g, r.gamma);

        let V = if wp { wr } else if {-wr};

        return P, V
    }
}
