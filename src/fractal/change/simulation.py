"""

    *Simulation Parameters*

  Parameters for parallel game simulations.

"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Vision:
    is_many_games: int
    is_many_workers: int
    is_batch_size: int

    shall_use_gpu: bool = False
    shall_fill_batches: bool = True
    shall_reset_every: Optional[int] = 1

    flip_probability: float = 0.0
    alternate_colors: bool = False


"""

These parameters are common to self-play data generation, neural network evaluation
and benchmarking.
  + On each machine (process), `num_workers` simulation tasks are spawned. Inference
    requests are processed by an inference server by batch of size `batch_size`. Note that
    we must have `batch_size <= num_workers`.
  + If `fill_batches` is set to `true`, we make sure that batches sent to the
    neural network for inference have constant size.
  + Both players are reset (e.g. their MCTS trees are emptied)
    every `reset_every` games (or never if `nothing` is passed).
  + To add randomization and before every game turn, the game board is "flipped"
    according to a symmetric transformation with probability `flip_probability`.
  + In the case of (symmetric) two-player games and if `alternate_colors` is set to`true`,
    then the colors of both players are swapped between each simulated game.

"""
