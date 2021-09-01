from __future__ import annotations
from typing import Iterator

from .step import Timestep


pub struct Time(
    Iterator<Timestep>,
):
    fn __iter__(&self) -> Time:
        return &self

    fn __next__(&self) -> Timestep:
        pass

    fn flow(&self) -> Timestep:
        return next(&self)