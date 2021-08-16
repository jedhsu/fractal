"""
Imagine
=======

"""

from typing import Callable

from fractal.world import World

from .._imagining import Imagining
from ..multiprocessing import Multiprocessing


class Imagine(
    Imagining,
):
    def imagine(
        self,
        world: World,
        multiprocessing: Multiprocessing,
        on_imagined: Callable,
    ):
        """
        This is simulate.
        """

    def imagine_parallely(
        self,
        world: World,
        multiprocessing: Multiprocessing,
        on_imagined: Callable,
    ):
        """
        This is distributed simulate.
        """
        pass
