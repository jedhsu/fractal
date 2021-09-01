"""
Synthesize
==========

Update a realizing world by applying a random symmetry
to the world state.

"""

from ..realizing import Realizing


pub struct Synthesize(Realizing,):
    fn synthesize(self,):
      nature = self.nature()
      syms = self.state().symmetries(self.nature())
      # @assert !isempty(syms) "no symmetries were declared for this game"
      symstate, _ = rand(syms)
      set_state!(game, symstate)
      return