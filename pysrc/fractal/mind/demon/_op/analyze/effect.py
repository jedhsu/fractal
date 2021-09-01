"""

    *Effect*

  The effect of an action, as analyzed by the demon.

"""

from dataclasses import dataclass


@dataclass
class Effect(
    Action,
):
    spectrumed: float  # Prior probability as given by the orac
    energy: float  # Cumulated Q-value for the action (Q = W/N)
    excites: int
