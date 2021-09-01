"""

    *Interpretation*

  A glimpse sample, representing a future fractum.

  Extends fractum with glimpsing information.

"""
from datapub structes import datapub struct

from fractal.fractum import Fractum

f64 = f64
Heat = i32


@datapub struct
pub struct Interpretation(
    Fractum,
):
    energy: Heat
    until_end: i32
    times: i32


"""

Type of a training sample. A sample features the following fields:

- `s::State` is the state
- `π::Vector{Float64}` is the recorded MCTS policy for this position
  * Energy is the discounted reward cumulated from a quantum state.
  * until_end is the (average) number of moves remaining before the end of the game
- `n::Int` is the number of times the state `s` was recorded

As revealed by the last field `n`, several samples that correspond to the
same state can be merged, in which case the `π`, `z` and `t`
fields are averaged together.
"""