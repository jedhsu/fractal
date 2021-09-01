"""

    *Pondered*

  Metrics generated after the self-play phase of an iteration.

"""

f64 = float


class Pondered:
    samples_gen_speed: f64
    average_exploration_depth: f64
    mcts_memory_footprint: int
    memory_size: int
    memory_num_distinct_boards: int


# def glimpsed(realization, _, player):
#     mem = MCTS.approximate_memory_footprint(player.mcts)
#     edepth = MCTS.average_exploration_depth(player.mcts)
#     return (trace=trace, mem=mem, edepth=edepth,)

"""


  sampling_frequency`: average number of samples generated per second
  average_exploration_depth: see [`MCTS.average_exploration_depth`](@ref)
  mcts_memory_footprint: estimation of the maximal memory footprint of the
    MCTS tree during self-play, as computed by
    [`MCTS.approximate_memory_footprint`](@ref)
  memory_size: number of samples in the memory buffer at the end of the
    self-play phase
  memory_num_distinct_boards: number of distinct board positions in the
    memory buffer at the end of the self-play phase

"""
