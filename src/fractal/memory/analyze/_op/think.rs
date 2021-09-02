//! Add a new (policy, reward, state) quadruple.

pub struct Thought {
    whisper: Whisper,
    reward: Reward,
    state: State,
}

pub trait Think {
    fn think(&self);
}

// impl  Think(
//     Thinking,
// ):
//     fn think(
//         &self,
//         state: WorldState,
//         daemon: Daemon,
//         energy: Energy,
//     ):
//         pass

//     fn _validate(&self):
//         pass

