//! Wisdom.

pub struct Wisdom {
    mcts: T,

    episodes: i32,
    //! The number of iterations of MCTS.
    
    timeout: Option<i32>,
    //!   - if `timeout` is provided, MCTS simulations are executed for `timeout` seconds
    //!     by groups of `niters`.
    time: Time<f64>,
}

impl Wisdom {
    fn emerge(
        nature: Nature,
        energy: Energy,
        age: i32,
        timeout: Option<Time>,
    ) {}
        // assert age > 0
        // assert timeout is None or timeout > 0

    // # return cls<A>((mcts, energy, niters, timeout, τ)
// }
}

//! MctsPlayer{MctsEnv} <: AbstractPlayer
//!
//! A player that selects actions using MCTS.

impl Imaginer {
    fn new(imagining: Imagining, temperature: usize, n: usize, timeout: usize) {}
    //! Construct a mind from a glimpsing loop.
    //!
    //! When computing each move:
    //!     
    //!   - otherwise, `niters` MCTS simulations are run
    
    fn from_demon(nature: Nature, demon: Demon, imagination: Imagination, timeout: usize) {}
    //! Construct an MCTS player from an oracle and an <`MctsParams`>(@ref) structure.

}

// TODO dont really get this
// \\\!
//     Benchmark.MctsRollouts(params) <: Benchmark.Player

// Pure MCTS baseline that uses rollouts to evaluate new positions.

// Argument `params` has type <`MctsParams`>(@ref).
// \\\!

pub struct Curiosity(Cortex,) {
    nature = FocusedNature
}

name(p::MctsRollouts) = "MCTS ($(p.params.num_iters_per_turn) rollouts)"

fn new(explored: Explored, nature: Nature, brain: Brain) {
    return Perspective {nature: Nature, Curiosity(nature), explored.parameters)
}
