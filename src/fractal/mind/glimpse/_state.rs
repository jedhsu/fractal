//! Glimpsed World State

pub struct GlimpsedState {
    actions: Iterator<GlimpsedAction>,
    energy: f64,
}

impl GlimpedState { 
    fn new(
        prior_probability: f64,
        energy: f64,
        prior_temperature,
    ):
        P = Util.apply_temperature(
            prior_probability,
            prior_temperature,
        )
        glimpsed_actions = {GlimpsedAction(prior, 0, 0) for prior in P}
        return GlimpsedState {glimpsed_actions, energy}

    fn num_visited(&self) -> i32 {
        sum(action.num_visited for action in &self.actions)
    }
}
