

"""
    params(::AbstractNetwork)

Return the collection of trainable parameters of a network.
"""
function params end

"""
    regularized_params(::AbstractNetwork)

Return the collection of regularized parameters of a network.
This usually excludes neuron's biases.
"""
function regularized_params end

"""
    num_parameters(::AbstractNetwork)

Return the total number of parameters of a network.
"""
function num_parameters(nn::AbstractNetwork)
  return sum(length(p) for p in params(nn))
end

"""
    num_regularized_parameters(::AbstractNetwork)

Return the total number of regularized parameters of a network.
"""
function num_regularized_parameters(nn::AbstractNetwork)
  return sum(length(p) for p in regularized_params(nn))
end
