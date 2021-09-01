"""

    *Dynamics*

"""

# Surprisingly, Flux does not like the following code (scalar operations):
# mse_wmean(ŷ, y, w) = sum((ŷ .- y).^2 .* w) / sum(w)


from dataclasses import dataclass

class Optimize:
def losses(
    brain: Brain,
    regularization: Regularization,
    evolution: Evolution,
    transition: Transition,
):
    pass
    # # `regws` must be equal to `Network.regularized_params(nn)`
    # creg = params.l2_regularization
    # cinv = params.nonvalidity_penalty
    # P̂, V̂, p_invalid = Network.forward_normalized(nn, X, A)
    # V = V ./ params.rewards_renormalization
    # V̂ = V̂ ./ params.rewards_renormalization
    # Lp = klloss_wmean(P̂, P, W) - Hp
    # Lv = mse_wmean(V̂, V, W)
    # Lreg = iszero(creg) ?
    # zero(Lv) :
    # creg * sum(sum(w .* w) for w in regws)
    # Linv = iszero(cinv) ?
    # zero(Lv) :
    # cinv * wmean(p_invalid, W)
    # L = (mean(W) / Wmean) * (Lp + Lv + Lreg + Linv)
    # return (L, Lp, Lv, Lreg, Linv)


def wmean(
    x,
    w,
):
    return sum(x * w) / sum(w)
