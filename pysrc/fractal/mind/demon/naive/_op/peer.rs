from .._demon import NaiveDemon


pub struct Peer(NaiveDemon):
    fn think(
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