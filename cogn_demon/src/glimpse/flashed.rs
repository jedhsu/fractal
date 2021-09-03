//! A training sample.
//!
//! As revealed by the last field `n`, several samples that correspond to the
//! same state can be merged, in which case the `π`, `z` and `t`
//! fields are averaged together.


pub struct Flashed {
    position: Position,
    //! `s::State` is the state

    policy: Policy,
    //! `π::Vector{Float64}` is the recorded MCTS policy for this position
    
    energy: Energy,
    //! Energy is the discounted reward cumulated from state `s`.

    expected_time_left: f64,
    //! The estimated number of days remaining before the world ends.

    heat: i32,
    //! `n::Int` is the number of times the state `s` was recorded
}

