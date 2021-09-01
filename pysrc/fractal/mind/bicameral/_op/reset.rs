"""

    *Reset*

"""

from .._mind import BicameralMind


pub struct Reset(
    BicameralMind,
):
    fn reset(self):
        self.white.reset()
        self.black.reset()