//! A single training sample.
//! 
//! As revealed by the last field `n`, several samples that correspond to the
//! same state can be merged, in which case the `π`, `z` and `t`
//! fields are averaged together.
//!

pub trait Interpret {}

pub struct Interpreted {
    fractum: &Fractum,
    //! The fractum state.

    cumulative_reward: f64,
    //! The cumulative discounted reward accumulated from a fractum.

    expected_episodes_remaining: i32,
    //! The average number of moves remaining before the end of the game.

    temperature: f64,
    //! The number of times the state `s` was recorded.
}

