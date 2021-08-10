"""

    *Flow*

"""

from .._mind import BicameralMind


class Flow(
    BicameralMind,
):
    def flow(
        self,
        spacetime: Spacetime,
        epoch: Epoch,
    ):
        if Flow.is_it_dawn(game):
            return self.white.flow(
                spacetime,
                epoch,
            )
        else:
            return self.black.flow(
                spacetime,
                epoch,
            )
