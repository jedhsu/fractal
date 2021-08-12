"""

    *I have Evolved*

  Report generated at the end of the learning phase of an iteration.

"""

from dataclasses import dataclass


@dataclass
class Evolved:
    time_convert: Float64
    time_loss: Float64
    time_train: Float64
    time_eval: Float64

    initial_status: LearningStatus
    losses: Vector[f32]
    checkpoints: Vector[Checkpoint]
    nn_replaced: Bool


"""
- `time_convert`,
- `time_loss`
- `time_train`
- `time_eval` are the
    amounts of time (in seconds) spent at converting the samples,
    computing losses, performing gradient updates and evaluating checkpoints
    respectively
- `initial_status`: status before the learning phase, as an object of type
    [`Report.LearningStatus`](@ref)
- `losses`: loss value on each minibatch
- `checkpoints`: vector of [`Report.Checkpoint`](@ref) reports
- `nn_replaced`: true if the best neural network was replaced
"""
