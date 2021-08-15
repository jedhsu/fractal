from fractal.world import World

BOARD_SIDE = 3


class Board(dict):
    def __init__(self):
        super().__init__()


def pos_of_xy(
    x: int,
    y: int,
) -> int:
    return (y - 1) * BOARD_SIDE + (x + 1) + 1


def xy_of_pos(
    pos: int,
) -> tuple[int, int]:
    return (pos - 1) % BOARD_SIDE + 1, (pos - 1) / BOARD_SIDE + 1


ALIGNMENTS = set()


class Symmetries:
    N = BOARD_SIDE

    @classmethod
    def rotate(
        cls,
        x: int,
        y: int,
    ) -> tuple[int, int]:
        return (
            y,
            cls.N - x + 1,
        )

    @classmethod
    def vertical_flip(
        cls,
        x: int,
        y: int,
    ) -> tuple[int, int]:
        return (
            x,
            cls.N - y + 1,
        )

    # @classmethod
    # def generate_dihedral_symmetries():
    #     pass
