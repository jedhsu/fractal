\\\!
World <End>
===========

Define the conditions in which the world ends.

\\\!

from typing import Callable

pub struct End(
    World,
):
    pass

pub struct Test:
    pub struct TicTacToe_End:
        fn is_full(&self):
            if 
        fn endings(&self) -> set<WorldState>:
            return WorldState.full()