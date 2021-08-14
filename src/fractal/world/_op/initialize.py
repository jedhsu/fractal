
from copy import deepcopy

from .._world import World

from ..nature import Nature

class Initialize(World,):
    @classmethod
    def initialize(cls, nature: Nature):
      env = nature.deepcopy()
      RL.reset!(env.rlenv)
      return env

# function GI.init(spec::Spec, state)
#   env = GI.clone(spec.env)
#   RL.setstate!(env.rlenv, state)
#   return env
# end
