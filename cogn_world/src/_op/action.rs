pub trait Action {
    fn from_ident(ident: ActionIdent) -> Option<Action>;
    //! Return the action described by string `str` or `nothing` if `str` does not
    //! denote a valid action.

}

impl Display for Action {
    fn display(&self) -> &str;
    /// Return a prettified representation of an action.

}

impl Parse for Action {
    fn action(&self)  -> Action;
}

// impl Action for World {
//     fn action_string(&&self) {}

//     fn parse_action(&&self) {}
// }
