"""

    Simulator(make_player, make_oracles, measure)

A distributed simulator that encapsulates the details of running simulations
across multiple threads and multiple machines.

# Arguments

  - `make_oracles`: a function that takes no argument and returns
      the oracles used by the player, which can be either `nothing`,
      a single oracle or a pair of oracles.
  - `make_player`: a function that takes as an argument the result of `make_oracles`
      and builds a player from it. In practice, an oracle returned by `make_oracles`
      may be replaced by a `BatchedOracle` before it is passed to `make_player`, which
      is why these two functions are specified separately.
  - `measure(trace, colors_flipped, player)`: the function that is used to
      take measurements after each game simulation.

"""

from dataclasses import dataclass

@dataclass
class Simulator(MakePlayer, Oracles, Measure):
    make_player :: MakePlayer
    make_oracles :: Oracles
    measure :: Measure
