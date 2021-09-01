"""
Realizing
=========

The environment of a game is the world in a realizing loop.

"""

from datapub structes import datapub struct

from .._world import World


@datapub struct
pub struct Realizing(
    World,
):
    state: WorldState
    time: WorldTime