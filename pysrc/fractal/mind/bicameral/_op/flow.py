"""

    *Flow*

"""

from .._mind import BicameralMind


pub struct Flow(
    BicameralMind,
):
    fn flow(
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