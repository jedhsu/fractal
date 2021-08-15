# """
#    TwoPlayers <: AbstractPlayer

# If `white` and `black` are two [`AbstractPlayer`](@ref), then
# `TwoPlayers(white, black)` is a player that behaves as `white` when `white`
# is to play and as `black` when `black` is to play.
# """

# flipped_colors(p::TwoPlayers) = TwoPlayers(p.black, p.white)

# function think(p::TwoPlayers, game)
#  if GI.white_playing(game)
#    return think(p.white, game)
#  else
#    return think(p.black, game)
#  end
# end

# function select_move(p::TwoPlayers, game, turn)
#  if GI.white_playing(game)
#    return select_move(p.white, game, turn)
#  else
#    return select_move(p.black, game, turn)
#  end
# end

# function reset!(p::TwoPlayers)
#  reset!(p.white)
#  reset!(p.black)
# end
