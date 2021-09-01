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
    //! Game specification
}


// TODO - PERTURB

// ## Dirichlet Noise

// A naive way to ensure exploration during training is to adopt an ϵ-greedy
// policy, playing a random move at every turn instead of using the policy
// prescribed by <`MCTS.policy`>(@ref) with probability ϵ.
// The problem with this naive strategy is that it may lead the player to make
// terrible moves at critical moments, thereby biasing the policy evaluation
// mechanism.

// A superior alternative is to add a random bias to the neural prior for the root
// node during MCTS exploration: instead of considering the policy ``p`` output
// by the neural network in the UCT formula, one uses ``(1-ϵ)p + ϵη`` where ``η``
// is drawn once per call to <`MCTS.explore!`>(@ref) from a Dirichlet distribution

