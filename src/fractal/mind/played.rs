//! The outcome of an episode.


pub struct Reward {
    base: Vec<f64>,
    extra: Vec<f64>,
}

pub struct Played {
    summary: str,
    //! A string describing the evaluation.

    reward_path: Vec<Reward>,
    //! The sequence of rewards collected by the evaluated player.
    //!   - Reflecting: `rewards` is the sequence of rewards collected by the evaluated player.
    //!   - Dueling: 
    
    baseline_reward_path: Option<Vec<Reward>>,
    //! The sequence of rewards collected by the baseline player.

    mean_reward: f64,
    //! Mean reward.
    //!   - Reflecting: Average reward is equal to `mean(rewards) - mean(baseline_rewards)`.
    
    redundancy: f64,
    //! The ratio of duplicate positions encountered during the evaluation,
    //! not counting the initial position.

    duration: f64,
    //! The accumulated computing time spent running the evaluation, in seconds.
}

impl Played {
    fn from_reflecting(reflecting: Reflecting) {}
    fn from_dueling(dueling: Dueling) {}
}
