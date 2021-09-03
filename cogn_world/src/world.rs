

pub trait Realizing: Flowing {};

pub trait World: A where A: Rules {
    pub type world: Realizing
}

impl World {
    fn two_players(&self) {
        // GI.two_players(spec::Spec) = spec.env.two_players
    }

    fn actions(&self) {
        // GI.actions(spec::Spec) = RL.actions(spec.env.rlenv)
    }
    
    fn vecorize_state(&self) {
        // spec.env.vectorize_state(spec.env.rlenv, state)
    }

// // pub struct Nature {
// //     world: World
// // }

// impl World {
//     fn new(nature: Nature) {
//         world = nature.clone();
//         RL.reset!(env.rlenv);
//         env;
//     }

//     fn initialize(nature: Nature, state: Realizing) {
//         world = nature.world.clone();
//         world.mind.interpret(state)
//     }
// }
