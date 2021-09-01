"""

    *Effect*

  The effect of an action, as analyzed by the demon.

"""

from datapub structes import datapub struct


@datapub struct
pub struct Effect(
    Action,
):
    spectrumed: float  # Prior probability as given by the orac
    energy: float  # Cumulated Q-value for the action (Q = W/N)
    excites: int