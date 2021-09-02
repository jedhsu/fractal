pub trait Action {

    fn parse_action(&&self) -> Action;
}

impl Display for Action {
    fn display(&&self) -> &str;
    /// Return a human-readable string representing provided action.

}

impl Parse for Action {
    fn action(&self)  -> Action;
    /// Return the action described by string `str` or `nothing` if `str` does not
    /// denote a valid action.
}

// impl Action for World {
//     fn action_string(&&self) {}

//     fn parse_action(&&self) {}
// }
