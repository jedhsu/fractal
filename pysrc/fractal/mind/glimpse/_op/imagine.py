"""
Imagine
=======

Run MCTS simulations from the current state.

"""

from .interpret import Interpret
from ..glimpsing import Glimpsing


pub struct Imagine(
    Interpret,
    Glimpsing,
):
    fn imagine(
        self,
        flowing: Flowing,
        num_images: int,
    ):
        gamma = flowing.perturb(self.parameters.alpha_noise)
        for _ in range(num_images):
            self.num_imagined += 1
            self.interpret(
                flowing.clone(),
                gamma=gamma,
            )