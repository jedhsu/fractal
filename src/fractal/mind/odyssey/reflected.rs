//! Metrics generated after the &self-play phase of an iteration.

pub struct Reflected {
    sampling_frequency: f64,
    //! The average number of samples generated per second.

    average_exploration_depth: f64,
    //! The estimated maximum memory footpri32 of the glimpse during &self-play

    mcts_memory_footpri32: i32,
    //! estimation of the maximal memory footpri32 of the glimpse

    memory_size: i32,
    //! number of samples in the memory buffer at the end of the &self-play phase

    memory_num_distinct_boards: i32,
    //! number of distinct board positions in the memory buffer at the end of the &self-play phase
}

