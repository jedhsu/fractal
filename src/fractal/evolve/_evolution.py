"""

    *Evolution - Learning*

  Parameters governing the learning phase of a training iteration, where
  the neural network is updated to fit the data in the memory buffer.

"""

from dataclasses import dataclass


@dataclass
class Evolution:
    shall_use_gpu: bool
    shall_use_position_averaging: bool

    samples_weighing_policy: SamplesWeighingPolicy
    optimization: Optimization

    l2_regularization: float
    rewards_renormalization: float
    nonvalidity_penalty: float
    batch_size: int
    loss_computation_batch_size: int
    min_checkpoints_per_epoch: int
    max_batches_per_checkpoint: int
    count_checkpoints: int


class Default:
    pass


"""
  The neural network goes through `num_checkpoints` series of `n` updates using
  batches of size `batch_size` drawn from memory, where `n` is defined as follows:

```
n = min(max_batches_per_checkpoint, ntotal ÷ min_checkpoints_per_epoch)
```

with `ntotal` the total number of batches in memory. Between each series,
the current network is evaluated against the best network so far
(see [`ArenaParams`](@ref)).

+ `nonvalidity_penalty` is the multiplicative constant of a loss term that
   corresponds to the average probability weight that the network puts on
   invalid actions.
+ `batch_size` is the batch size used for gradient descent.
+ `loss_computation_batch_size` is the batch size that is used to compute
  the loss between each epochs.
+ All rewards are divided by `rewards_renormalization` before the MSE loss is computed.
+ If `use_position_averaging` is set to true, samples in memory that correspond
  to the same board position are averaged together. The merged sample is
  reweighted according to `samples_weighing_policy`.

# AlphaGo Zero Parameters

In the original AlphaGo Zero paper:
+ The batch size for gradient updates is ``2048``.
+ The L2 regularization parameter is set to ``10^{-4}``.
+ Checkpoints are produced every 1000 training steps, which corresponds
  to seeing about 20% of the samples in the memory buffer:
  ``(1000 × 2048) / 10^7  ≈ 0.2``.
+ It is unclear how many checkpoints are taken or how many training steps
  are performed in total.
"""
