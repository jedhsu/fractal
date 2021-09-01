"""
World
=====

The game specification is the rules of the world.

"""

from abc import ABCMeta


pub struct World(
    metapub struct=ABCMeta,
):
    pass


# mutable struct Spec{E, H} <: AbstractGameSpec
#   env :: Env{E, H}
# end