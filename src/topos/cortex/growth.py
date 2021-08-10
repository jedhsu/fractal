

"""
    OptimiserSpec

Abstract type for an optimiser specification.
"""
abstract type OptimiserSpec end

"""
    CyclicNesterov(; lr_base, lr_high, lr_low, momentum_low, momentum_high)

SGD optimiser with a cyclic learning rate and cyclic Nesterov momentum.

  - During an epoch, the learning rate goes from `lr_low`
    to `lr_high` and then back to `lr_low`.
  - The momentum evolves in the opposite way, from high values
    to low values and then back to high values.
"""
@kwdef struct CyclicNesterov <: OptimiserSpec
  lr_base :: Float32
  lr_high :: Float32
  lr_low  :: Float32
  momentum_low :: Float32
  momentum_high :: Float32
end

"""
    Adam(;lr)

Adam optimiser.
"""
@kwdef struct Adam <: OptimiserSpec
  lr :: Float32
end

"""
    train!(callback, ::AbstractNetwork, opt::OptimiserSpec, loss, batches, n)

Update a given network to fit some data.
  - [`opt`](@ref OptimiserSpec) specifies which optimiser to use.
  - `loss` is a function that maps a batch of samples to a tracked real.
  - `data` is an iterator over minibatches.
  - `n` is the number of minibatches. If `length` is defined on `data`,
     we must have `length(data) == n`. However, not all finite
     iterators implement `length` and thus this argument is needed.
  - `callback(i, loss)` is called at each step with the batch number `i`
     and the loss on last batch.
"""
function train! end
