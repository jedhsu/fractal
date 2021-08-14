"""

    *Peer*

  Return a single possible flow of spacetime. A default implementation is provided that samples
  an action according to the distribution computed by [`think`](@ref), with a
  temperature given by [`player_temperature`](@ref).

"""


class Peer:
    def peer(
        self,
        topos: Topos,
        epoch: int,
    ):
        fractum = player.glimpsing(game)
        energy = player, energy(game, turn_number)
        demon = self.apply_energy()
        return actions[Util.rand_categorical(π)]
