//!! Information gathered from a glimpse.
//!
//! the &self-play phase of an iteration

pub struct Glimpsed {
    glimpsing_frequency: f64,
    //! Average number of samples generated per second.

    average_steps_ahead: f64,
    //!

    estimated_dream_scale: i32,
    //! estimation of the maximal memory footpri32 of the
    //! MCTS tree during &self-play, as computed by
    //! <`MCTS.approximate_memory_footpri32`>(@ref)
    //! &self-play phase
    
    number_of_glimpsed: i32.
    //! number of samples in the memory buffer at the end of the

    number_of_unique_realized: i32,
    //! number of distinct board positions in the
    //! memory buffer at the end of the &self-play phase
}

// impl Glimpsed {
//     fn new(reali
// }

fn glimpsed(demon: Demon) {
    let mem = .estimated_memory_load(demon.glimpser());
    let edepth = Foresight.average_exploration_depth(demon.glimpser());
    (trace=trace, mem=mem, edepth=edepth,)
}

