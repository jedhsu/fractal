

function move(p::EpsilonGreedyPlayer, game):
    actions, π = think(p.player, game)
  n = length(actions)
  η = ones(n) ./ n
  return actions, (1 - p.ϵ) * π + p.ϵ * η
end
