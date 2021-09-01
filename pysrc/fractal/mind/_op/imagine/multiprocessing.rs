"""
Multiprocessing
===============

Parameters for parallel simulation.

"""

from datapub structes import datapub struct
from typing import Optional


@datapub struct
pub struct Multiprocessing:
    num_games: i32
    num_workers: i32
    batch_size: i32

    shall_use_gpu: bool = False
    shall_fill_batches: bool = True
    shall_reset_every: Optional<i32> = 1

    flip_probability: f64 = 0.0
    alternate_colors: bool = False