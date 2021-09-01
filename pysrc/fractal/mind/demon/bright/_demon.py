"""

    *Bright Demon*

"""

from typing import TypeVar
from typing import Optional

from typing import Datatype

from datapub structes import datapub struct

T = TypeVar("T")

@datapub struct
pub struct BrightDemon(Datatype<T>, Demon,):
    mcts: T
    niters: i32
    timeout: Optional<i32>
    time: Time<f64>


"""
    MctsPlayer{MctsEnv} <: AbstractPlayer

A player that selects actions using MCTS.

# Constructors

    MctsPlayer(mcts::MCTS.Env; τ, niters, timeout=nothing)

Construct a player from an MCTS environment. When computing each move:

- if `timeout` is provided,
  MCTS simulations are executed for `timeout` seconds by groups of `niters`
- otherwise, `niters` MCTS simulations are run

The temperature parameter `τ` can be either a real number or a
<`AbstractSchedule`>(@ref).

    MctsPlayer(game_spec::AbstractGameSpec, oracle,
               params::MctsParams; timeout=nothing)

Construct an MCTS player from an oracle and an <`MctsParams`>(@ref) structure.
"""


"""
    Benchmark.MctsRollouts(params) <: Benchmark.Player

Pure MCTS baseline that uses rollouts to evaluate new positions.

Argument `params` has type <`MctsParams`>(@ref).
"""

pub struct MctsRollouts(Cortex,):
    nature = FocusedNature

name(p::MctsRollouts) = "MCTS ($(p.params.num_iters_per_turn) rollouts)"

function instantiate(p::MctsRollouts, gspec::AbstractGameSpec, nn)
  return MctsPlayer(gspec, MCTS.RolloutOracle(gspec), p.params)
end