from __future__ import annotations
from typing import Iterator

from .step import Timestep


class Time(
    Iterator[Timestep],
):
    def __iter__(self) -> Time:
        return self

    def __next__(self) -> Timestep:
        pass

    def flow(self) -> Timestep:
        return next(self)
