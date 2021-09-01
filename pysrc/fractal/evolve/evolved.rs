//! Report generated at the end of the learning phase of an iteration.

pub struct Evolved {
    /// Amount of time (in seconds) spent at converting the samples.
    time_convert: f64,
    /// Amount of time (in seconds) spent at computing the losses.
    time_loss: f64,
    /// Amount of time (in seconds) spent at performing gradient updates.
    time_train: f64,
    /// Amount of time (in seconds) spent at evaluating checkpoints.
    time_eval: f64,
    /// `initial_status`: status before the learning phase, as an object of type
    /// [`Report.LearningStatus`](@ref)
    initial_status: LearningStatus,
    /// `losses`: loss value on each minibatch
    losses: Vec<f32>,
    /// `checkpoints`: vector of [`Report.Checkpoint`](@ref) reports
    checkpoints: Vec<Checkpoint>,
    /// `nn_replaced`: true if the best neural network was replaced
    nn_replaced: bool,
}
