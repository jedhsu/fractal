"""

    *Nature*

  The rules of the world.

"""


class Physics:
    pass

mutable struct Spec{E, H} <: AbstractGameSpec
  env :: Env{E, H}
end
