"""

    *Reset*

"""

from .._mind import BicameralMind


class Reset(
    BicameralMind,
):
    def reset(self):
        self.white.reset()
        self.black.reset()
