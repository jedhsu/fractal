//! The outcome of a duel.

pub struct Dueled {
    emcee: str,
    //! A string describing the evaluation.

    contentment: f64,
    //! Average of euphoria.

    redundancy: f64,
    //! The ratio of duplicate positions encountered during the
    //! evaluation, not counting the initial position. If this number is too high,
    //! you may want to increase the move selection temperature.

    euphoria: Euphoria,
    //! The sequence of rewards collected by the evaluated player.

    duration: f64,
    //! The accumulated computing time spent running the evaluation, in seconds.
}
