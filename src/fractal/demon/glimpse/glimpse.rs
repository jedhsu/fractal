//! A MCTS is Glimpse.
//! 
//! Parameters for the glimpse.

pub struct DirichletNoise {
    epsilon: f64,
    alpha: f64,
}

pub struct Glimpse {
    patience: f64,
    //! the reward discount factor

    skepticism: f64,
    //! exploration constant in the UCT formula
    
    noise: DirichletNoise,
    /// parameters for the dirichlet exploration noise

    temperature: f64,
    //! temperature to apply to the oracle's output to get
    //! the prior probability vector used by MCTS.
}

impl Default for Glimpse {
    fn default() {
        Glimpse { patience: 1.0, skepticism: 1.0, DirichletNoise {epsilon: 1.0, alpha: 1.0}, temperature: 1.0}
    }
}
