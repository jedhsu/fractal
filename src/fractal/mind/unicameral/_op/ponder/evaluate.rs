//! Evaluate a single neural network for a one-player game.

impl Evaluate for Pondering {
    fn evaluate(
        nature: Nature,
        brain: Brain,
        evaluation: Evaluation,
        clock: AtDusk,
    ) {
        make_oracles = brain.copy(
            on_gpu=Fractal.Mind.Imagination.use_gpu,
            test_mode=true,
        )
        let simulator = Simulator(make_oracles, record_trace) do oracle
        let simulator.MctsPlayer(gspec, oracle, params.mcts)

        let samples = simulate()
        simulator, gspec, params.sim,
        game_simulated=(() -> Handlers.checkpoi32_game_played(handler))
        rewards_and_redundancy(samples, gamma=params.mcts.gamma,)
    }
}

# Single-player Games

- `rewards` is the sequence of rewards collected by the evaluated player
- `baseline_rewards` is the sequence of rewards collected by the baseline player
- `avgr` is equal to `mean(rewards) - mean(baseline_rewards)`
