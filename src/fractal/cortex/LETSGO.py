


"""
    game_spec(::AbstractNetwork)

Return the game specification that was passed to the network's constructor.
"""
function game_spec end

to_singletons(x) = reshape(x, size(x)..., 1)
from_singletons(x) = reshape(x, size(x)[1:end-1])


#####
##### Derived functions
#####

"""
    mean_weight(::AbstractNetwork)

Return the mean absolute value of the regularized parameters of a network.
"""
function mean_weight(nn::AbstractNetwork)
  sw = sum(sum(abs.(p)) for p in regularized_params(nn))
  sw = convert_output(nn, sw)
  return sw / num_regularized_parameters(nn)
end



"""
    forward(::AbstractNetwork, states)

Compute the forward pass of a network on a batch of inputs.

Expect a `Float32` tensor `states` whose batch dimension is the last one.

Return a `(P, V)` triple where:

  - `P` is a matrix of size `(num_actions, batch_size)`. It is allowed
    to put weight on invalid actions (see [`evaluate`](@ref)).
  - `V` is a row vector of size `(1, batch_size)`
"""

function forward end




"""
    convert_output(::AbstractNetwork, output)

Convert an array (or number) produced by a neural network
to a standard CPU array (or number) type.
"""
function convert_output end

function convert_output_tuple(
    nn::AbstractNetwork, output::Union{Tuple, NamedTuple})
  return map(output) do arr
    convert_output(nn, arr)
  end
end

"""
    gc(::AbstractNetwork)

Perform full garbage collection and empty the GPU memory pool.
"""
function gc end

