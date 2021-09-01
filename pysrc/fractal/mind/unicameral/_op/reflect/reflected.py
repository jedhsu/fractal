"""
Reflected
=========

Metrics generated after the self-play phase of an iteration.

"""

from datapub structes import datapub struct

f64 = f64


@datapub struct
pub struct Reflected:
    sampling_frequency: f64
    average_exploration_depth: f64
    mcts_memory_footpri32: i32
    memory_size: i32
    memory_num_distinct_boards: i32


"""

    `sampling_frequency`
      average number of samples generated per second

    `average_exploration_depth`
      estimation of the maximal memory footpri32 of the glimpse during self-play
    
    `memory_footpri32`
      estimation of the maximal memory footpri32 of the glimpse
    
    `memory_size`
      number of samples in the memory buffer at the end of the self-play phase

    `memory_num_distinct_boards`
      number of distinct board positions in the memory buffer at the end of the self-play phase

"""