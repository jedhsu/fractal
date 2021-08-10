

"""
    HyperParams(::Type{<:AbstractNetwork})

Return the hyperparameter type associated with a given network type.
"""
function HyperParams end

"""
    hyperparams(::AbstractNetwork)

Return the hyperparameters of a network.
"""
function hyperparams end

"""
    game_spec(::AbstractNetwork)

Return the game specification that was passed to the network's constructor.
"""
function game_spec end

"""
    to_gpu(::AbstractNetwork)

Return a copy of the given network that has been transferred to the GPU
if one is available. Otherwise, return the given network untouched.
"""
function to_gpu end

"""
    to_cpu(::AbstractNetwork)

Return a copy of the given network that has been transferred to the CPU
or return the given network untouched if it is already on CPU.
"""
function to_cpu end

"""
    on_gpu(::AbstractNetwork) :: Bool

Test whether or not a network is located on GPU.
"""
function on_gpu end

"""
    set_test_mode!(mode=true)

Put a network in test mode or in training mode.
This is relevant for networks featuring layers such as
batch normalization layers.
"""
function set_test_mode! end

"""
    convert_input(::AbstractNetwork, input)

Convert an array (or number) to the right format so that it can be used
as an input by a given network.
"""
function convert_input end

function convert_input_tuple(
    nn::AbstractNetwork, input::Union{Tuple, NamedTuple})
  return map(input) do arr
    convert_input(nn, arr)
  end
end


"""
A generic, framework agnostic interface for neural networks.
"""
module Network

export AbstractNetwork, OptimiserSpec, CyclicNesterov, Adam

using ..AlphaZero

using Base: @kwdef
using Statistics: mean

import Flux  # we use Flux.batch

"""
    AbstractNetwork

Abstract base type for a neural network.

# Constructor

Any subtype `Network` must implement `Base.copy` along with
the following constructor:

    Network(game_spec, hyperparams)

where the expected type of `hyperparams` is given by
[`HyperParams(Network)`](@ref HyperParams).
"""
abstract type AbstractNetwork end

#####
##### Interface
#####
