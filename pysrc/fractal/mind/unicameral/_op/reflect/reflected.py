"""
Reflected
=========

Metrics generated after the self-play phase of an iteration.

"""

from dataclasses import dataclass

f64 = float


@dataclass
class Reflected:
    sampling_frequency: f64
    average_exploration_depth: f64
    mcts_memory_footprint: int
    memory_size: int
    memory_num_distinct_boards: int


"""

    `sampling_frequency`
      average number of samples generated per second

    `average_exploration_depth`
      estimation of the maximal memory footprint of the glimpse during self-play
    
    `memory_footprint`
      estimation of the maximal memory footprint of the glimpse
    
    `memory_size`
      number of samples in the memory buffer at the end of the self-play phase

    `memory_num_distinct_boards`
      number of distinct board positions in the memory buffer at the end of the self-play phase

"""
