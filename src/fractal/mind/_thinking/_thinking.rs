//! Collects all world states visited during a lifetime.

pub struct Thinking {
    // WorldState,
    // ):
    states: Sequence<WorldState>,
    demons: Vec<Demon>,
    thermodynamics: Vec<Energy>,
}