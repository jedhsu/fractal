"""

    *Pondered*

  Metrics generated after the self-play phase of an iteration.

"""

f64 = f64


pub struct Pondered:
    samples_gen_speed: f64
    average_exploration_depth: f64
    mcts_memory_footpri32: i32
    memory_size: i32
    memory_num_distinct_boards: i32


# fn glimpsed(realization, _, player):
#     mem = MCTS.approximate_memory_footpri32(player.mcts)
#     edepth = MCTS.average_exploration_depth(player.mcts)
#     return (trace=trace, mem=mem, edepth=edepth,)

"""


  sampling_frequency`: average number of samples generated per second
  average_exploration_depth: see <`MCTS.average_exploration_depth`>(@ref)
  mcts_memory_footpri32: estimation of the maximal memory footpri32 of the
    MCTS tree during self-play, as computed by
    <`MCTS.approximate_memory_footpri32`>(@ref)
  memory_size: number of samples in the memory buffer at the end of the
    self-play phase
  memory_num_distinct_boards: number of distinct board positions in the
    memory buffer at the end of the self-play phase

"""