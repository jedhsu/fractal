//! Statistics about the performance of the neural network on a subset of the
//! memory buffer.

pub struct EvolutionStatus {
    /// `loss`: detailed loss on the samples, as an object of type
    /// [`Report.Loss`](@ref)
    loss: Loss,
    /// `Hp`: average entropy of the ``π`` component of samples (MCTS policy);
    /// this quantity is independent of the network and therefore constant
    /// during a learning iteration
    entropy: f32,
    /// `Hpnet`: average entropy of the network's prescribed policy on the samples
    average_entropy: f32,
}