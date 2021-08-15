from .nature import Nature


class World:
    nature: Nature


# function Env(
#     rlenv :: RL.AbstractEnv;
#     heuristic_value = default_heurisic_value,
#     vectorize_state = default_vectorize_state,
#     symmetries      = default_symmetries,
#     render          = default_render,
#     action_string   = default_action_string,
#     parse_action    = default_parse_action,
#     read_state      = default_read_state)
#   nplayers = length(RL.players(rlenv))
#   @assert nplayers == 1 || nplayers == 2 "
#   AlphaZero.jl only supports games with one or two players."
#   two_players = nplayers == 2
#   return Env(
#     rlenv, 0., two_players,
#     heuristic_value, vectorize_state, symmetries,
#     render, action_string, parse_action, read_state)
# end
