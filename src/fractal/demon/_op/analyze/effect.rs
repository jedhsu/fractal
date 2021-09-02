\\\!

    *Effect*

  The effect of an action, as analyzed by the demon.

\\\!

from datapub structes import datapub struct


@datapub struct
pub struct Effect(
    Action,
):
    spectrumed: f64  # Prior probability as given by the orac
    energy: f64  # Cumulated Q-value for the action (Q = W/N)
    excites: i32