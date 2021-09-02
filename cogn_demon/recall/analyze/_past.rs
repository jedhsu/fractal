//! The past consists of all world states visited during a lifetime.

pub struct Past {
    // WorldState,
    // ):
    history: Vec<State>,
    daemon: Vec<Demon>,
    work: Vec<Energy>,
}
