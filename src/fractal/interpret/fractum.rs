//! Type of a training sample. A sample features the following fields:
//! *Interpretation*
//! A glimpse sample, representing a future fractum.
//! Extends fractum with glimpsing information.

pub trait Interpret {}

pub struct Interpreted {
    fractum: &Fractum,

    energy: Heat,
    //! The discounted reward cumulated from a quantum state.

    steps_until_end: i32,
    //! The average number of moves remaining before the end of the game.

    count: i32,
    //! The number of times the state `s` was recorded.
}

// \\\!

// - `s::State` is the state
// - `π::Vector{Float64}` is the recorded MCTS policy for this position

// As revealed by the last field `n`, several samples that correspond to the
// same state can be merged, in which case the `π`, `z` and `t`
// fields are averaged together.
// \\\!

