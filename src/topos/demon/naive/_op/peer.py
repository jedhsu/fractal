from .._demon import NaiveDemon


class Peer(NaiveDemon):
    def think(
        self,
        mind: Mind,
    ):
        actions = Spacetime.available_actions(game)
        n = len(actions)
        spectrum = ones(n) / len(actions)
        return Place(
            actions,
            spectrum,
        )
