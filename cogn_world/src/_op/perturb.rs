mod perturb {
    fn sample_dirichlet_noise(
        realizing: Realizing,
        noise: Noise,
    ) {
        actions = world.possible_actions()
        n = len(actions)
        return rand(Dirichlet(n, noise))
    }
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

