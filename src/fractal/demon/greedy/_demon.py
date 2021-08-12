"""

    *Greedy Demon*

  Greedy.

  A wrapper on a player that makes it choose a random move
  with a fixed ``ϵ`` probability.

"""

from dataclasses import dataclass
from .._demon import Demon

@dataclass
class GreedyDemon(Generic[P], Demon,):
    player :: P
    epsilon :: Float64

function player_temperature(self, world: World, epoch: Epoch,):
    return player_temperature(p.player, game, turn)
