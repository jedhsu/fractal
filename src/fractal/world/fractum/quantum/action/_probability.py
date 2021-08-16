"""
Quantum Probability
===================

"""


class QuantumProbability(
    int,
):
    def __init__(
        self,
        probability: int,
    ):
        super().__new__(
            int,
            probability,
        )
