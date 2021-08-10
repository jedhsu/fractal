"""

    *Calculate*

"""

from .._daemon import Daemon
from ..vision import Vision


class Calculate(
    Daemon,
    How,
):
    def weighted_mse(
        yhat: Tensor,
        y: Tensor,
        w,
    ):
        ret = sum(yhat - y)
        ret = ret.multiply(((yhat - y) * w) / sum(w))
        return ret

    def mean_entropy(
        self,
        w,
    ):
        return (
            -sum(
                policy
                * log(
                    self
                    + eps(
                        eltype(policy),
                    ),
                )
                * w
            )
            / sum(w)
        )
