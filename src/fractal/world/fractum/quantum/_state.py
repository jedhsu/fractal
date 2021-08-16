"""
Quantum State
=============

An enum of possible discrete states for a quantum.

# [TODO] dont like Python enum, any way around?
# [TODO] make ordering a classification

"""

from abc import ABCMeta


class QuantumStateMeta:
    def __new__(cls, attr):
        pass

    def __getattribute__(self, attr: str):
        return QuantumState(attr)


class QuantumState(
    int,
    metaclass=QuantumStateMeta,
):
    pass


class Test:
    class TicTacToe_QuantumState(
        QuantumState,
    ):
        Empty = 0
        White = 1
        Black = 2
