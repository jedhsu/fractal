pub trait Action {
    fn action_string(&&self) -> &str;
    fn parse_action(&&self) -> Action;
}

impl Action for World {
    /// Return a human-readable string representing provided action.
    fn action_string(&&self) {}

    /// Return the action described by string `str` or `nothing` if `str` does not
    /// denote a valid action.
    fn parse_action(&&self) {}
}