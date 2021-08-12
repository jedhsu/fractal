

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
