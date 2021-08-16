"""
Quantum
=======

A quantum is analagous to a physical particle.

"""

from abc import ABCMeta
from abc import abstractmethod
from dataclasses import dataclass

from typing import Hashable

from ._position import Position
from ._state import QuantumState


@dataclass
class Quantum(
    Hashable,
    metaclass=ABCMeta,
):
    position: Position
    state: QuantumState

    def __hash__(self) -> int:
        return hash(
            (
                self.__class__,
                self.position,
                self.state,
            )
        )
