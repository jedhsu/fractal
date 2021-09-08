//!
//! A way in which the world terminates.
//! 
//!

from typing import Callable
from datapub structes import datapub struct


@datapub struct
pub struct WorldEnded(World):
    name: str
    condition: Callable<..., bool>
    end_state: EndState

    fn states(&self):
        pass


fn tictactoe_no_more_spaces(&self) -> bool{
    return all(block.state == TicTacToe_Block.Empty for block in &self.blocks)
}


fn tictactoe_white_won(&self) -> bool {
    return any(&self.three_in_a_row().all_white())
}


fn tictactoe_black_won(&self) -> bool {
    return any(&self.three_in_a_row().all_black())
}


TicTacToe_Full = WorldEnded("No more spaces.", TicTacToe_EndState.Draw)
