//! Describes the results of a Glimpse.
pub struct Glimpsed {
    glimpsing_frequency: f64,
    //! Average number of samples generated per second.
    //! TODO is this infer_frequency?

    average_steps_ahead: f64,
    //!

    estimated_dream_scale: i32,
    //! estimation of the maximal memory footpri32 of the
    //! MCTS tree during &self-play, as computed by
    //! <`MCTS.approximate_memory_footpri32`>(@ref)
    //! &self-play phase
    
    number_glimpsed: i32.
    //! number of samples in the memory buffer at the end of the

    unique_number_realized: i32,
    //! number of unique board positions in the
    //! memory buffer at the end of the &self-play phase
}

// impl Glimpsed {
//     fn new(reali
// }
