

pub enum Player {
    White,
    Black,
}

pub struct Space {

}

pub struct Position {
    x: i32,
    y: i32,
}

impl Position {
    fn from_index(idx: u64) {
        Position((pos - 1) % BOARD_SIDE + 1, (pos - 1) / BOARD_SIDE + 1)
    }
    fn into_index(&self) -> u64 {
        (position.y - 1) * BOARD_SIDE + (position.x + 1) + 1
    }
}

pub struct Nature {
    board_side = 3;
    num_positions = board_side ** 2


    Cell: type = Optional[bool]
    Board: type = Matrix[num_positions, Cell]  # can implement in tensor pkg
    initial_board = Board.empty()
    initial_state = WorldState(Board, Mind.White)
}


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


ALIGNMENTS = set()


class TicTacToe(
    World,
):
    def action_string(self):
        pass

    def parse_action(self, string):
        pass
