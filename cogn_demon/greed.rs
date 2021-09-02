//! Greed chooses a random move 
//! with a fixed `ϵ` probability.

pub struct Greed {
    epsilon: f64
}

pub trait Flow {
    fn temperature(&self, world: &Realizing);
    fn think(&self, world: &Realizing);
    fn reset(&self);
}

impl Flow {


impl Flow for Greed {
    fn temperature(&self, world: Realizing) {
        return player_temperature(p.player, game, turn)
    }

    fn think(&self, world: &Realizing) {
        let (actions, whisper) = &self.mind.think(world);

        let n = actions.len();
        let eta = n.ones() ./ n;

        (actions, (1 - self.epsilon) * whisper + &self.noise.epsilon * eta)
    }

    fn reset(&self) {
        p.player.reset()
    }
}
