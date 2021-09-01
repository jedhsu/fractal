"""
Imagine
=======

Run MCTS simulations from the current state.

"""

from .i32erpret import Interpret
from ..glimpsing import Glimpsing


pub struct Imagine(
    Interpret,
    Glimpsing,
):
    fn imagine(
        self,
        flowing: Flowing,
        num_images: i32,
    ):
        gamma = flowing.perturb(self.parameters.alpha_noise)
        for _ in range(num_images):
            self.num_imagined += 1
            self.i32erpret(
                flowing.clone(),
                gamma=gamma,
            )