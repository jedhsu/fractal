"""

    *Lattice*

  The focused mind overfits.

  (SimpleNet)

"""


from dataclasses import dataclass

@dataclass
class Lattice(Architecture):
    width: int
    depth_common: int
    depth_phead: int = 1
    depth_vhead: int = 1
    use_batch_norm: bool = false
    batch_norm_momentum: f32 = 0.6

Network.HyperParams(::Type{SimpleNet}) = SimpleNetHP

"""
"""


"""
width       Number of neurons on each lattice layer.

| `depth_common: Int`         | Number of dense layers in the trunk          |
| `depth_phead = 1`         Number of hidden layers in the actions head 
| `depth_vhead = 1`             | Number of hidden layers in the value  head   |
| `use_batch_norm = false`      | Use batch normalization between each layer   |
| `batch_norm_momentum = 0.6f0` | Momentum of batch norm statistics updates    |

