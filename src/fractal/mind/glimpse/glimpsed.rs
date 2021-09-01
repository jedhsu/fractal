//!! Information gathered from a glimpse.
//!
//! the &self-play phase of an iteratio

pub struct Glimpsed {
    sampling_frequency: f64,
    //! Average number of samples generated per second.

    average_exploration_depth: f64,
    //!

    mcts_memory_footpri32: i32,
    //! estimation of the maximal memory footpri32 of the
    //! MCTS tree during &self-play, as computed by
    //! <`MCTS.approximate_memory_footpri32`>(@ref)
    //! &self-play phase
    
    memory_size: i32.
    //! number of samples in the memory buffer at the end of the

    memory_num_distinct_boards: i32,
    //! number of distinct board positions in the
    //! memory buffer at the end of the &self-play phase
}

// impl Glimpsed {
//     fn new(reali
// }

// # fn glimpsed(realization, _, player):
// #     mem = MCTS.approximate_memory_footpri32(player.mcts)
// #     edepth = MCTS.average_exploration_depth(player.mcts)
// #     return (trace=trace, mem=mem, edepth=edepth,)

