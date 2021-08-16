"""
Quantum Action
==============
A possible action of a quantum.

A quantum action is either a
* motion to a new position,
* change to a new state,

potentially conditional on an action.

"""

from abc import ABCMeta

from dataclasses import dataclass
from typing import Optional

from .._quantum import Quantum
from ._probability import QuantumProbability


@dataclass
class QuantumAction(
    Quantum,
    metaclass=ABCMeta,
):
    condition: Optional[Action]
    probability: QuantumProbability
