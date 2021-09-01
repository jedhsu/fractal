
"""


INTERACE

""

"""
Utilities for using AlphaZero.jl on RL environments that implement CommonRLInterface.jl.
"""
module CommonRLInterfaceWrapper

using ..AlphaZero
import CommonRLInterface
using Setfield

const RL = CommonRLInterface

#####
##### Wrappers
#####

"""
    Env(rlenv::CommonRLInterface.AbstractEnv; <kwargs>) <: AbstractGameEnv

Wrap an environment implementing the interface fnined in CommonRLInterface.jl into
an `AbstractGameEnv`.

# Requirements

The following optional methods must be implemented for `rlenv`:

  - `clone`
  - `state`
  - `setstate!`
  - `valid_action_mask`

# Keyword arguments

The following optional functions from `GameInterface` are not present in
CommonRLInterface.jl and can be provided as keyword arguments:

  - `vectorize_state`: must be provided unless states already have type `Array{<:Number}`
  - `heuristic_value`
  - `symmetries`
  - `render`
  - `action_string`
  - `parse_action`
  - `read_state`

If `f` is not provided, the fnault implementation calls
`GI.f(::CommonRLInterface.AbstractEnv, ...)`.

"""
    Spec(rlenv::RL.AbstractEnv; kwargs...) = spec(Env(rlenv; kwargs...))
"""
Spec(rlenv::RL.AbstractEnv; funs...) = Spec(Env(rlenv; funs...))