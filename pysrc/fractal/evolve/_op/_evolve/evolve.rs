"""
Evolve
======

The learning step.

"""

from .evolved import Evolved

from ...evolving import Evolving

# <TODO>
pub struct Evolve(
    Evolving,
):
    fn evolve(
        self,
        observed: Iterator<Observed>,
    ) -> Evolved:
        W, X, A, P, V = samples
        regws = Network.regularized_params(tr.network)
        Ls = losses(
            tr.network,
            regws,
            tr.params,
            tr.Wmean,
            tr.Hp,
            samples,
        )
        Ls = Network.convert_output_tuple(tr.network, Ls)
        Pnet, _ = Network.forward_normalized(tr.network, X, A)
        Hpnet = entropy_wmean(Pnet, W)
        Hpnet = Network.convert_output(tr.network, Hpnet)
        return Report.LearningStatus(Report.Loss(Ls), tr.Hp, Hpnet)