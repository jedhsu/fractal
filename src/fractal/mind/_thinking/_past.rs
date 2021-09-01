//! The past consists of all world states visited during a lifetime.

pub struct Past {
    // WorldState,
    // ):
    history: Vec<WorldState>,
    demons: Vec<Demon>,
    thermodynamics: Vec<Energy>,
}
