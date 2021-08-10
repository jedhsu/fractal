

# Evaluate a single neural network for a one-player game (params::ArenaParams)
def evaluate_network(physics: Physics, unicortex: Unicortex, speech: Speech, handler,):
    make_oracles = nnet.copy(net, on_gpu=params.sim.use_gpu, test_mode=true,)

    simulator = Simulator(make_oracles, record_trace)
    simulator.MctsPlayer(gspec, oracle, params.mcts)

    samples = simulate()
    simulator, gspec, params.sim,
    game_simulated=(() -> Handlers.checkpoint_game_played(handler))
    return rewards_and_redundancy(samples, gamma=params.mcts.gamma,)
