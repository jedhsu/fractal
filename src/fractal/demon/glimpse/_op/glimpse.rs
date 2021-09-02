//!  Return a glimpse, a single possible flow of the next state in time.
//!
//!  A default implementation is provided that sample an action according to the
//!  distribution computed by <`think`>(@ref), with a temperature given by
//!  <`player_temperature`>(@ref).


pub trait Flow {
    fn glimpse(&self, realizing: Realizing);

    fn reset(&self);
    //! Reset the glimpse by emptying the MCTS tree.

}

impl Glimpse {
    fn glimpse(
        &self,
        realizing: Realizing,
    ) {
        let fractum = player.glimpsing(game)
        let energy = player, energy(game, turn_number)
        let demon = &self.apply_energy()
        actions<Util.rand_categorical(π)>
    }

    fn reset(&self) {
        &self.tree = dict()
    }
}
