//! Report generated at the end of the learning phase of an iteration.

pub struct Evolved {
    time_convert: f64,
    //! Amount of time (in seconds) spent at converting the samples.

    time_loss: f64,
    //! Amount of time (in seconds) spent at computing the losses.

    time_train: f64,
    //! Amount of time (in seconds) spent at performing gradient updates.

    time_eval: f64,
    //! Amount of time (in seconds) spent at evaluating checkpoints.

    initial_status: LearningStatus,
    //! `initial_status`: status before the learning phase, as an object of type
    //! [`Report.LearningStatus`](@ref)

    losses: Vec<f32>,
    //! `losses`: loss value on each minibatch

    checkpoints: Vec<Checkpoint>,
    //! `checkpoints`: vector of [`Report.Checkpoint`](@ref) reports

    nn_replaced: bool,
    //! `nn_replaced`: true if the best neural network was replaced
}
