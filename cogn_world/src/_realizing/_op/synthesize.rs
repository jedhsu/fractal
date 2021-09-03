//! Update a realizing world by applying a random symmetry

pub trait Synthesize {
    fn synthesize(&self);
}

impl Synthesize for Realizing {
    fn synthesize(&self) {
        let nature = &self.nature();
        let syms = &self.state().symmetries(&self.nature());

        // @assert !isempty(syms) "no symmetries were declared for this game"
        // symstate, _ = rand(syms);
        set_state!(game, symstate);
    }
}
