"""
    evaluate_batch(::AbstractNetwork, batch)

Evaluate the neural network as an MCTS oracle on a batch of states at once.

"""
class Evaluate(Brain,):
    def evaluate_batch(self, batch,):
        gspec = game_spec(nn)
        X = Flux.batch((GI.vectorize_state(gspec, b) for b in batch))
        A = Flux.batch((GI.actions_mask(GI.init(gspec, b)) for b in batch))
        Xnet, Anet = convert_input_tuple(nn, (X, Float32.(A)))
        P, V, _ = convert_output_tuple(nn, forward_normalized(nn, Xnet, Anet))
        return [(P[A[:,i],i], V[1,i]) for i in eachindex(batch)]

"""

Take a list of states as input and return a list of `(P, V)` pairs as defined in the
MCTS oracle interface.

"""

"""
    forward_normalized(network::AbstractNetwork, states, actions_mask)

Evaluate a batch of vectorized states. This function is a wrapper
on [`forward`](@ref) that puts a zero weight on invalid actions.

# Arguments

  - `states` is a tensor whose last dimension has size `bach_size`
  - `actions_mask` is a binary matrix of size `(num_actions, batch_size)`

# Returned value

Return a `(P, V, Pinv)` triple where:

  - `P` is a matrix of size `(num_actions, batch_size)`.
  - `V` is a row vector of size `(1, batch_size)`.
  - `Pinv` is a row vector of size `(1, batch_size)`
     that indicates the total probability weight put by the network
     on invalid actions for each sample.

All tensors manipulated by this function have elements of type `Float32`.
"""
function forward_normalized(nn::AbstractNetwork, state, actions_mask)
  p, v = forward(nn, state)
  p = p .* actions_mask
  sp = sum(p, dims=1)
  p = p ./ (sp .+ eps(eltype(p)))
  p_invalid = 1 .- sp
  return (p, v, p_invalid)
end
