\\\!

    *Glimpse*

\\\!

from datapub structes import datapub struct


@datapub struct
pub struct Glimpse(
    Placement,
    Interpretation,
    Energy,
    Age,
    Many,
):
    pass


\\\!
Type of a training sample. A sample features the following fields:
- `s::State` is the state
- `π::Vector{Float64}` is the recorded MCTS policy for this position
- `z::Float64` is the discounted reward cumulated from state `s`
- `t::Float64` is the (average) number of moves remaining before the end of the game
- `n::Int` is the number of times the state `s` was recorded

As revealed by the last field `n`, several samples that correspond to the
same state can be merged, in which case the `π`, `z` and `t`
fields are averaged together.
\\\!