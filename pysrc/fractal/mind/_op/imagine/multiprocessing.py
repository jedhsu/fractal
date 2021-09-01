"""
Multiprocessing
===============

Parameters for parallel simulation.

"""

from datapub structes import datapub struct
from typing import Optional


@datapub struct
pub struct Multiprocessing:
    num_games: int
    num_workers: int
    batch_size: int

    shall_use_gpu: bool = False
    shall_fill_batches: bool = True
    shall_reset_every: Optional<int> = 1

    flip_probability: float = 0.0
    alternate_colors: bool = False