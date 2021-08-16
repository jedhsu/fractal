"""
Measure
=======

"""

from .._thinking import Thinking


class Measure(
    Thinking,
):
    def __len__(self):
        return len(self.thermodynamics)

    def total_energy(self):
        pass
