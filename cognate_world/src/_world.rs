
from abc import ABCMeta


// pub struct World(
//     metapub struct=ABCMeta,
// ):
//     pass


// pub struct Nature {
//     world: World
// }

impl World {
    fn new(nature: Nature) {
        world = nature.clone();
        RL.reset!(env.rlenv);
        env;
    }

    fn initialize(nature: Nature, state: Realizing) {
        world = nature.world.clone();
        world.mind.interpret(state)
    }
}
