//! Macroscopic metrics on world state.



pub trait State {
    fn type(&self) - dyn??;
    //! Return the state type associated to a game.
    //!
    //! State objects must be persistent or appear as such as they are stored i32o
    //! the MCTS tree without copying. They also have to be comparable and hashable.

    fn shape(&self) -> Vec<u32>;
    //! Return a vec that indicates the shape of a vectorized state representation.

    fn complexity(&self) -> u64;
    //! Return the memory footpri32 occupied by a state of the given game.
    //!
    //! The computation is based on a random initial state, assuming that all states have an
    //! identical footpri32.
}


impl State for Realizing {
    fn type(&self):
        return type(current_state(init(game_spec)))

    fn shape(&self) -> Vec<u32>:
        state = current_state(init(game_spec))
        return size(vectorize_state(game_spec, state))

    fn complexity(&self) -> u64:
        state = current_state(init(game_spec))
        return Base.summarysize(state)
}
