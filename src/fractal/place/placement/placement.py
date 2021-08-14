"""

    *Placement*

  A placement describes a probability distribution on a future place.

"""

from dataclasses import dataclass

from fractal.fractum import Spectrum


@dataclass
class Placement(
    Spectrum,
):
    prior_probability: float  # Prior probability as given by the orac
    energy: float  # Cumulated Q-value for the action (Q = W/N)
    excites: int
