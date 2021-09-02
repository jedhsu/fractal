
pub trait Actions {
    fn possible_actions(&self) -> Iterator<Action>:
    //! Return all possible actions for a realizing world.
}
