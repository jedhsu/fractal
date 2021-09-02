//! The demon of greed chooses a random move 
//! with a fixed `ϵ` probability.

pub struct Greed {
    epsilon: f64
}

pub trait Flow {
    fn temperature(&self, realizing: Realizing);
    fn move(&self, realizing: Realizing);
}

impl Flow {
fn temperature(&self, realizing: Realizing):
    return player_temperature(p.player, game, turn)

fn move(&self, realizing: Realizing) {
    actions, π = think(p.player, game)
    n = length(actions)
    η = ones(n) ./ n
    actions, (1 - p.ϵ) * π + p.ϵ * η
}
