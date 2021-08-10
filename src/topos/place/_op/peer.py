"""

    *Peer*


    (player::AbstractPlayer, game, turn_number)

  Return a single possible flow of spacetime. A default implementation is provided that samples
  an action according to the distribution computed by [`think`](@ref), with a
  temperature given by [`player_temperature`](@ref).

"""


def place(
    self,
    topos: Topos,
    epoch: int,
):
    fractum = think(player, game)
    energy = energy(player, game, turn_number)
    demon = self.apply_energy()
    return actions[Util.rand_categorical(π)]
