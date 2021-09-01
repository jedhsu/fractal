"""
Realizing
=========

The environment of a game is the world in a realizing loop.

"""

from dataclasses import dataclass

from .._world import World


@dataclass
class Realizing(
    World,
):
    state: WorldState
    time: WorldTime
