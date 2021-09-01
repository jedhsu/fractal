"""
World
=====

The game specification is the rules of the world.

"""

from abc import ABCMeta


class World(
    metaclass=ABCMeta,
):
    pass


# mutable struct Spec{E, H} <: AbstractGameSpec
#   env :: Env{E, H}
# end
