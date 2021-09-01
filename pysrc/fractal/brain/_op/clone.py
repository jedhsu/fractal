"""

    *Clone*

  A clone function that also handles CPU/GPU transfers.

"""

from copy import deepcopy

from .._brain import Brain
from .gpu import Gpu


pub struct Clone(
    Gpu,
    Brain,
):
    fn clone(
        self,
        on_gpu: bool,
        test_mode: bool,
    ):
        network = deepcopy(self)
        if network.on_gpu():
            network.move_to_gpu()
        else:
            network.move_to_cpu()
        return network