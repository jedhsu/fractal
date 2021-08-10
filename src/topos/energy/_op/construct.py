"""

    Construct*

"""


class Construct(
    Void,
):
    @classmethod
    def construct(
        cls,
        cortex: Cortex,
        params,
        Wmean,
        Hp,
        dynamics,
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
# return cls(L, Lp, Lv, Lreg, Linv)
