"""
Compute
=======

Computations for optimization.

"""

from funcy import flow

import numpy as np

from operator import add
from operator import times
from operator import div

from ..void import Void

from math import log


class Compute:
    @staticmethod
    def weighted_mse(
        yhat: np.array,
        y: np.array,
        w,
    ):
        ret = sum(yhat - y)
        ret = ret.multiply(((yhat - y) * w) / sum(w))
        return ret

    @sm
    def mean_entropy(
        self,
        w,
    ):
        return -sum(policy * log(demon + eps(eltype(policy))) * w) / sum(w)

    @staticmethod
    def klloss_weighted_mse(
        angel: Daemon,
        demon: Daemon,
        focus: Weights,
    ):
        return -sum(demon * log(angel + eps(eltype(demon))) * focus) / sum(focus)
