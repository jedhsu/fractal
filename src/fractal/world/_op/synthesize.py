"""

    *Synthesize*

  Update a game environment by applying a random symmetry
  to the current state (see [`symmetries`](@ref)).

"""

from .._world import World

from .state import State

class Synthesize(State, World,):
    def synthesize(self,):
      nature = self.nature()
      syms = self.state().symmetries(self.nature())
      # @assert !isempty(syms) "no symmetries were declared for this game"
      symstate, _ = rand(syms)
      set_state!(game, symstate)
      return

