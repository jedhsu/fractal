//! Update world state.

pub trait Realize {
    fn realize(&self, state: State);
}

impl Realize for Realizing {
    fn realize(&self, state: State) {}
}

