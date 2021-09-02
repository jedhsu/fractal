//! A training sample.
//!
//! As revealed by the last field `n`, several samples that correspond to the
//! same state can be merged, in which case the `π`, `z` and `t`
//! fields are averaged together.


pub struct Flashed {
    position: Position,
    //! `s::State` is the state

    whisper: Whisper,
    //! `π::Vector{Float64}` is the recorded MCTS policy for this position
    
    energy: Heat,
    //! `z::Float64` is the discounted reward cumulated from state `s`

    time_until_death: i32,
    //! `t::Float64` is the (average) number of moves remaining before the end of the game

    heat: i32,
    //! `n::Int` is the number of times the state `s` was recorded
}

