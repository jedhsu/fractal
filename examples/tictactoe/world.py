from fractal.world import World
from typing import Callable
from typing import Optional

from dataclasses import dataclass


class WorldState:
    position: WorldPosition
    time: WorldTime


class Mind:
    White = "White"
    Black = "Black"


class Statics:
    board_side = 3
    num_positions = board_side ** 2

    Player: type = bool
    white = True
    black = False

    Cell: type = Optional[bool]
    Board: type = Matrix[num_positions, Cell]  # can implement in tensor pkg
    initial_board = Board.empty()
    initial_state = WorldState(Board, Mind.White)


class Nature(
    AbstractNature,
):
    pass


class World(
    Nature,
    AbstractWorld,
):
    pass


class Board(dict):
    def __init__(self):
        super().__init__()


@dataclass
class Position:
    x: int
    y: int


def pos_of_xy(position: Position) -> int:
    return (position.y - 1) * BOARD_SIDE + (position.x + 1) + 1


def xy_of_pos(
    pos: int,
) -> Position:
    return Position((pos - 1) % BOARD_SIDE + 1, (pos - 1) / BOARD_SIDE + 1)


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

    @classmethod
    def ap(cls, fn: Callable) -> Callable:
        def inner(pos: int):
            return pos_of_xy(fn(xy_of_pos(pos)))

        return inner

    @classmethod
    def sym(cls, fn: Callable) -> Callable:
        pass

    # @classmethod
    # def generate_dihedral_symmetries():
    #     pass


class TicTacToe(
    World,
):
    def action_string(self):
        pass

    def parse_action(self, string):
        pass
