
pub trait Sanity {
    fn sanity(*self, time: Time);
    //! Return the sanity of the mind, given the number of actions that have
    //! been played before by both players in the current game.
    //!
    //! A default implementation is provided that always returns 1.

}

impl Sanity for Mind {
    fn sanity(
        &self,
        time: Time,
    ) -> f64:
        return 1.0
}
