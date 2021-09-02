//! A MCTS is Glimpse.
//! 
//! Parameters for the glimpse.

pub struct DirichletNoise {
    epsilon: f64,
    alpha: f64,
}

pub struct Glimpse {
    number_of_glimpsed_paths: u16,
    //! Number of imagines per day.

    skepticism: f64,
    //! The discount factor on future reward (gamma).

    curiosity: f64,
    //! The exploration constant in the upper-confidence-threshold formula.
    
    noise: DirichletNoise,
    /// Parameters for the dirichlet exploration noise.

    temperature: Schedule,
    //! The temperature to apply to the oracle's output to get
    //! the prior probability vector used by MCTS.
    //!
    //! It is typical to use a high value of the temperature parameter ``τ``
    //! during the first moves of a game to increase exploration and then switch to
    //! a small value.
    
    previous_temperature: f64,
}

impl Default for Glimpse {
    fn default() {
        Glimpse { patience: 1.0, skepticism: 1.0, DirichletNoise {epsilon: 1.0, alpha: 1.0}, temperature: 1.0}
    }

    fn alpha0() {
        //! Defaults from the original AlphaZero paper.
        //! + The number of MCTS iterations per move is 1600, which
        //!   corresponds to 0.4s of computation time.

        Glimpse { glimpsed_paths_per_episode: 1600, discount: 1., upper_confidence_threshold: 1.0, temperature: Schedule(), noise: DiricihletNoise {epsilon: 0.25, alpha: 0.03} }
    }
}

//! An MCTS player picks an action as follows.
//!
//! Given a game state, it launches `num_iters_per_turn` MCTS iterations, with UCT exploration constant `cpuct`.
//! Rewards are discounted using the `gamma` factor.
//!
//! Then, an action is picked according to the distribution ``π`` where ``π_i ∝ n_i^{1/τ}`` with ``n_i`` the number
//! of times that the ``i^{\\text{th}}`` action was visited and ``τ`` the `temperature` parameter.
//!
//! Therefore, `temperature` is am <`AbstractSchedule`>(@ref).
//!
//! For information on parameters `cpuct`, `dirichlet_noise_ϵ`
//!
//! `dirichlet_noise_α` and `prior_temperature`, see <`MCTS.Env`>(@ref).
//!
//!
//! + The temperature is set to 1 for the 30 first moves and then to an
//!   infinitesimal value.
//!
//! + The `ϵ` parameter for the Dirichlet noise is set to ``0.25`` and
//!   the ``α`` parameter to ``0.03``, which is consistent with the heuristic
//!   of using ``α = 10/n`` with ``n`` the maximum number of possibles moves,
//!   which is ``19 × 19 + 1 = 362`` in the case of Go.
