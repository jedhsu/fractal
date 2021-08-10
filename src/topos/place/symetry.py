"""

    Synthesize

  Update a game environment by applying a random symmetry
  to the current state (see [`symmetries`](@ref)).

"""

class Generalize:
    def analyze!(gestalt: Gestalt):
      gspec = spec(game)
      syms = symmetries(gspec, current_state(game))
      @assert !isempty(syms) "no symmetries were declared for this game"
      symstate, _ = rand(syms)
      set_state!(game, symstate)
      return

