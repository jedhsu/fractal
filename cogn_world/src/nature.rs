//! Specifies the laws of the world, such as initial and terminal conditions.

pub trait Nature {
    fn initial_time() -> Time;
    fn initial_state() -> State;
    fn has_world_ended() -> bool;
}
