//! A MCTS is Glimpse.
//! 
//! Parameters for the glimpse.

pub struct Noise {
    /// parameters for the dirichlet exploration noise
    epsilon: f64,
    alpha: f64,
}

pub struct Glimpse {
    const patience: f64 = 1.0,
    //! the reward discount factor

    const skepticism: f64 = 1.0,
    //! exploration constant in the UCT formula
    
    const noise: Noise,

    const sanity_before: f64,
    //! temperature to apply to the oracle's output to get
    //! the prior probability vector used by MCTS.
}
