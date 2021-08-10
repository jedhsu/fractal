# Evaluate a single neural network for a one-player game (params::ArenaParams)
def thinking(
    gestalt: Gestalt,
    architecture: Architecture,
    world: World,
    handler,
):
    make_oracles = architecture.copy(
        net,
        on_gpu=params.sim.use_gpu,
        test_mode=true,
    )
    # simulator = Simulator(make_oracles, record_trace) do oracle
    # simulator.MctsPlayer(gspec, oracle, params.mcts)

    # samples = simulate()
    # simulator, gspec, params.sim,
    # game_simulated=(() -> Handlers.checkpoint_game_played(handler))
    # return rewards_and_redundancy(samples, gamma=params.mcts.gamma,)
