"""

    *Demon*

  The managers of the brain with a policy and foresight.

  They have the power to interpret fractums.

"""

from fractum import Fractum

from abc import ABCMeta
from dataclasses import dataclass


@dataclass
class Demon(
    Fractum,
    metaclass=ABCMeta,
):
    depth: int
    age: float
    gamma: float
    shall_amplify: bool


# abstract type AbstractPlayer end

######
###### AlphaZero player
######

# function guess_mcts_arena_params(env::Env)
#  p = env.params
#  return isnothing(p.arena) ? p.self_play.mcts : p.arena.mcts
# end

# function guess_use_gpu(env::Env)
#  p = env.params
#  return isnothing(p.arena) ? p.self_play.sim.use_gpu : p.arena.sim.use_gpu
# end
