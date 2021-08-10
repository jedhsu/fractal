"""

    *Thinking Mind*

A player that uses the policy output by a neural network directly,
instead of relying on MCTS. The given neural network must be in test mode.
"""
struct NetworkPlayer{N} <: AbstractPlayer
  network :: N
end

function think(p::NetworkPlayer, game)
  actions = GI.available_actions(game)
  state = GI.current_state(game)
  π, _ = p.network(state)
  return actions, π
end
