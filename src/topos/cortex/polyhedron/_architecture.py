"""

    *Polyhedron*

  The residual network is isomorphic to a polyhedron. [CONFIRM]

"""

from torch import nn


class Polyhedron(
    nn.Sequential,
):
    pass


@dataclass
class PolyhedralMind:
    spacetime: Spacetime
    gestalt: Gestalt
    common
    vhead
    phead


class PolyhedronGestalt:
    nlayers: int
    nfilters: int
    kernel_shape: tuple[int, int]
    num_policy_head_filters: int = 2
    num_value_head_filters: int = 1
    batch_norm_momentum: float = 0.6


"""



The trunk of the two-head network consists of `num_blocks` consecutive blocks.
Each block features two convolutional layers with `num_filters` filters and
with kernel size `conv_kernel_size`. Note that both kernel dimensions must be
odd.

During training, the network is evaluated in training mode on the whole
dataset to compute the loss before it is switched to test model, using
big batches. Therefore, it makes sense to use a high batch norm momentum
(put a lot of weight on the latest measurement).

# AlphaGo Zero Parameters

The network in the original paper from Deepmind features 20 blocks with 256
filters per convolutional layer.

"""
