//! Reset by emptying the MCTS tree.

pub trait Reset {
    fn reset(&self);
}

impl Reset for Glimpsing {
    fn reset(&self) {
        &self.tree = dict()
    }
}

