\\\!

    *Observeds*

\\\!

# pub struct Observeds:
#     sample_weights: np.
#     world_representations:

\\\!
# A samples collection is represented on the learning side as a (W, X, A, P, V)
# named-tuple. Each component is a `Float32` tensor whose last dimension corresponds
# to the sample index. Writing `n` the number of samples and `a` the total
# number of actions:
# - W (size 1×n) contains the samples weights
# - X (size …×n) contains the board representations
# - A (size a×n) contains the action masks (values are either 0 or 1)
# - P (size a×n) contains the recorded MCTS policies
# - V (size 1×n) contains the recorded values
# Note that the weight of a sample is computed as an increasing
# function of its `n` field.
\\\!