//! Stateful data of a Glimpse.
//! MCTS.Env(game_spec::AbstractGameSpec, oracle; <keyword args>)
//!
//! Create and initialize an MCTS environment with a given `oracle`.
//! of parameter ``α``.


pub struct Glimpsing(
    Glimpse,
):
    tree: dict<State, StateInfo>,
    //! Store (nonterminal) state statistics assuming the white player is to play

    demon: MetaDemon,
    //! External oracle to evaluate positions

    total_simulations: u64,
    total_nodes_traversed: u64,
    //! Performance statistics

    nature: Nature,
    //! World specification
}

