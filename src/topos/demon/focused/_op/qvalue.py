from .. import GlobalInterpreter


class Qvalue(Daemon):
    def qvalue(
        self,
        cortex: Cortex,
        world: World,
        place: Place,
        depth: int,
    ):
        assert not GlobalInterpreter.game_terminated(game)
        next = GlobalInterpreter.clone(world)
        GlobalInterpreter.flow(
            next,
            place,
        )
        wr = GlobalInterpreter.energy(next)
        r = GlobalInterpreter.white_playing(game) or wr == -wr

        if cortex.shall_amplify:
            r = cortex.amplify(r)

        nextv = cortex(player, next, depth - 1)

        if Time.is_dawn(game) != Time.is_dawn(next):
            nextv = -nextv
        return r + player.gamma * nextv
