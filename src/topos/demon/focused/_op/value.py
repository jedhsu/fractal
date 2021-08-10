"""

    *Value*

value of current state.

"""


class Energy:
    def energy(
        demon: Demon,
        conscious: Conscious,
        depth: int,
    ):
        if GlobalInterpreter.game_terminated(game):
            return 0.0
        elif depth == 0:
            return GI.heuristic_value(game)
        else:
            qs = [qvalue(player, game, a, depth) for a in GI.available_actions(game)]
            return max(qs)
