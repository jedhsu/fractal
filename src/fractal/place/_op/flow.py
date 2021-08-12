
#####
##### Players can play against each other
#####

"""
    play_game(gspec::AbstractGameSpec, player; flip_probability=0.) :: Trace

Simulate a game by an [`AbstractPlayer`](@ref).

- For two-player games, please use [`TwoPlayers`](@ref).
- If the `flip_probability` argument is set to ``p``, the board
  is _flipped_ randomly at every turn with probability ``p``,
  using [`GI.apply_random_symmetry!`](@ref).
"""
function play_game(gspec, player; flip_probability=0.)
  game = GI.init(gspec)
  trace = Trace(GI.current_state(game))
  while true
    if GI.game_terminated(game)
      return trace
    end
    if !iszero(flip_probability) && rand() < flip_probability
      GI.apply_random_symmetry!(game)
    end
    actions, π_target = think(player, game)
    τ = player_temperature(player, game, length(trace))
    π_sample = apply_temperature(π_target, τ)
    a = actions[Util.rand_categorical(π_sample)]
    GI.play!(game, a)
    push!(trace, π_target, GI.white_reward(game), GI.current_state(game))
  end
end
