//! Evaluate a single neural network for a one-player game.

pub struct Evaluate(
    Mind,
):
    @pub structmethod
    fn thinking(
        cls,
        nature: Nature,
        brain: Brain,
        evaluation: Evaluation,
        handler: AtDusk,
    ):
        make_oracles = brain.copy(
            on_gpu=Fractal.Mind.Imagination.use_gpu,
            test_mode=true,
        )
        # simulator = Simulator(make_oracles, record_trace) do oracle
        # simulator.MctsPlayer(gspec, oracle, params.mcts)

        # samples = simulate()
        # simulator, gspec, params.sim,
        # game_simulated=(() -> Handlers.checkpoi32_game_played(handler))
        # return rewards_and_redundancy(samples, gamma=params.mcts.gamma,)