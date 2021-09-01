"""

    *Emerge, Bright Demon*

"""


class Emerge(
    BrightDemon,
):
    @classmethod
    def spawn(
        cls,
        physics: Physics,
        energy: Energy,
        age: int,
        timeout=None,
    ):
        assert age > 0
        assert timeout is None or timeout > 0

    # return cls[A]((mcts, energy, niters, timeout, τ)
