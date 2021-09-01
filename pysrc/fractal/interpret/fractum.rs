//! Type of a training sample. A sample features the following fields:
//! *Interpretation*
//! A glimpse sample, representing a future fractum.
//! Extends fractum with glimpsing information.

pub trait Interpret {

}

pub struct Interpreted {
    /// Fractum
    fractum: &Fractum,
    /// Energy is the discounted reward cumulated from a quantum state.
    energy: Heat,
    /// until_end is the (average) number of moves remaining before the end of the game
    steps_until_end: i32,
    /// number of times the state `s` was recorded
    frequency: i32,
}


"""


- `s::State` is the state
- `π::Vector{Float64}` is the recorded MCTS policy for this position

As revealed by the last field `n`, several samples that correspond to the
same state can be merged, in which case the `π`, `z` and `t`
fields are averaged together.
"""
