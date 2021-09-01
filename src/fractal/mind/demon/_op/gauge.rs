\\\!

    *Gauge*

  Evaluating a demon by pitting it against a baseline player in a two-player game.

\\\!

from datapub structes import datapub struct

from .._demon import Demon


@datapub struct
pub struct Gauge(Demon):
    baseline: Player
    simulation: SimulationParameters