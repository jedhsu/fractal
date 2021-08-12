"""

    *Dawn*

  Report generated after a checkpoint evaluation.

"""

from dataclasses import dataclass


@dataclass
class Dawn:
    batch_id: Int
    evaluation: Evaluation
    status_after: LearningStatus
    has_cortex_reincarnated: bool


"""
- `batch_id`: number of batches after which the checkpoint was computed
- `evaluation`: evaluation report from the arena, of type [`Report.Evaluation`](@ref)
- `status_after`: learning status at the checkpoint, as an object of type
   [`Report.LearningStatus`](@ref)
- `nn_replaced`: true if the current best neural network was updated after
   the checkpoint
"""
