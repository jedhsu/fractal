"""

    *Reset*

"""

from .._mind import BicameralMind


class Reset(
    BicameralMind,
):
    def reset(self):
        reset(self.white)
        reset(self.black)
