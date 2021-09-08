pub struct Position {
    state: PositionState,
}

pub enum PositionState {
    White,
    Black,
    Empty,
}

impl Fractum for Position {
    pub enum State {
        White,
        Black,
        Empty,
    }
}


pub struct Test:
    //! In Tic-Tac-Toe, a block quantum is not allowed to move. It can only switch states
    //! conditional on the player selecting the action.

    pub struct TicTacToeBlockActions(
        QuantumAction,
    ):
        fn actions(
            &self,
            action_space: type,
        ) -> set<QuantumAction> {
            actions = set()

            # <TODO> explore changing this to type level
            actions.add(
                QuantumAction(
                    &self.position,
                    &self.action.Circle,
                    condition=Action.place_circle(position),
                )
            )
            return actions }
        }
}
