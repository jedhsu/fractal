//! Return the mind sanity, given the number of actions that have
//! been played before by both players in the current game.

from .._demon import Demon


pub trait Sanity {
    fn energy(
        &self,
        realizing: Realizing,
        epoch: i32,
    ) -> f64:
        return 1.0
}
