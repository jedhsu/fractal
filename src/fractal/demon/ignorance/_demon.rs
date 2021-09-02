//! Ignorance randomly selects actions with equal probability.

// pub trait Ignorance: Demon {
// }
//     pass

// pub trait Ignorance: Demon {
//     fn temperature(&self, realizing: Realizing) -> Temperature;
//     fn think(&self, realizing: Realizing) -> Action;
//     fn move(&self, realizing: Realizing);
// }

impl Ignorance for Demon {
    fn temperature(&self, realizing: Realizing) {};
    fn think(&self, realizing: Realizing) {
        let actions = realizing.possible_actions();
        let n = actions.len();
        let spectrum = n.ones() / actions.len();

        Place(actions, spectrum)
    }
}
