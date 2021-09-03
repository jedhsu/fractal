

pub trait Realizing: Flowing {};

pub trait World: A where A: Rules {
    pub type world: Realizing
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
