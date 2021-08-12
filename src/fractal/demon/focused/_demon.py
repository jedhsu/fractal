"""

    *Focused Demon*

"""


"""

A simple implementation of the minmax tree search algorithm, to be used as
a baseline against AlphaZero. Heuristic board values are provided by the
[`GameInterface.heuristic_value`](@ref) function.

"""



amplify(r) = iszero(r) ? r : Inf * sign(r)

function minmax(player, game, actions, depth)
  return argmax([qvalue(player, game, a, player.depth) for a in actions])
end

"""
    MinMax.Player <: AbstractPlayer

A stochastic minmax player, to be used as a baseline.

    MinMax.Player(;depth, amplify_rewards, τ=0.)

The minmax player explores the game tree exhaustively at depth `depth`
to build an estimate of the Q-value of each available action. Then, it
chooses an action as follows:

- If there are winning moves (with value `Inf`), one of them is picked
  uniformly at random.
- If all moves are losing (with value `-Inf`), one of them is picked
  uniformly at random.

Otherwise,

- If the temperature `τ` is zero, a move is picked uniformly among those
  with maximal Q-value (there is usually only one choice).
- If the temperature `τ` is nonzero, the probability of choosing
  action ``a`` is proportional to ``e^{\\frac{q_a}{Cτ}}`` where ``q_a`` is the
  Q value of action ``a`` and ``C`` is the maximum absolute value of all
  finite Q values, making the decision invariant to rescaling of
  [`GameInterface.heuristic_value`](@ref).

If the `amplify_rewards` option is set to true, every received positive reward
is converted to ``∞`` and every negative reward is converted to ``-∞``.
"""
