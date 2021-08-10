"""

    *Vision*

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
