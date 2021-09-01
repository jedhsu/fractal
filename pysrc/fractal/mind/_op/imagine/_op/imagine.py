"""
Imagine
=======

"""

from typing import Callable

from fractal.world import World

from .._imagining import Imagining
from ..multiprocessing import Multiprocessing


pub struct Imagine(
    Imagining,
):
    fn imagine(
        self,
        world: World,
        multiprocessing: Multiprocessing,
        on_imagined: Callable,
    ):
        """
        This is simulate.
        """

    fn imagine_parallely(
        self,
        world: World,
        multiprocessing: Multiprocessing,
        on_imagined: Callable,
    ):
        """
        This is distributed simulate.
        """
        pass