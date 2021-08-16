"""
Evaluation
==========

"""

from dataclasses import dataclass

from fractal.glimpse import Glimpse
from fractal.mind.processing import Multiprocessing


@dataclass
class Evaluation:
    glimpse: Glimpse
    multiprocessing: Multiprocessing
