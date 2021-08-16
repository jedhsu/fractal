"""

    *Dusk*

  Report generated after a step.

"""

from dataclasses import dataclass


@dataclass
class Dusk:
    batch_id: int
    evaluated: Evaluated
    evolved: Evolved
    has_brain_refreshed: bool


"""

    `batch_id`
      number of batches after which the checkpoint was computed

    `evaluated`
      evaluation report

    `evolved`: learning status at the checkpoint, as an object of type

    `has_brain_refreshed`
      true if the current best neural network was updated after the checkpoint

"""
