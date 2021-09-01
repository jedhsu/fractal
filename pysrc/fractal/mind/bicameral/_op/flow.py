"""

    *Flow*

"""

from .._mind import BicameralMind


class Flow(
    BicameralMind,
):
    def flow(
        self,
        world: World,
        epoch: int,
    ):
        if world.is_it_dawn(game):
            return self.white.flow(
                spacetime,
                epoch,
            )
        else:
            return self.black.flow(
                spacetime,
                epoch,
            )
