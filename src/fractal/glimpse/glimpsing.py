"""
Glimpsing
=========

Environment for MCTS.

"""

"""
    MCTS.Env(game_spec::AbstractGameSpec, oracle; <keyword args>)

Create and initialize an MCTS environment with a given `oracle`.
of parameter ``α``.
"""


class Glimpsing(
    Glimpse,
):
    # Store (nonterminal) state statistics assuming the white player is to play
    tree: dict[State, StateInfo]

    # External oracle to evaluate positions
    demon: MetaDemon

    # Performance statistics
    total_simulations: u64
    total_nodes_traversed: u64

    # Game specification
    physics: Spacetime.Physics


"""
## Keyword Arguments

  - `gamma=1.`: the reward discount factor
  - `cpuct=1.`: exploration constant in the UCT formula
  - `noise_ϵ=0., noise_α=1.`: parameters for the dirichlet exploration noise
     (see below)
  - `prior_temperature=1.`: temperature to apply to the oracle's output
     to get the prior probability vector used by MCTS.

## Dirichlet Noise

A naive way to ensure exploration during training is to adopt an ϵ-greedy
policy, playing a random move at every turn instead of using the policy
prescribed by [`MCTS.policy`](@ref) with probability ϵ.
The problem with this naive strategy is that it may lead the player to make
terrible moves at critical moments, thereby biasing the policy evaluation
mechanism.

A superior alternative is to add a random bias to the neural prior for the root
node during MCTS exploration: instead of considering the policy ``p`` output
by the neural network in the UCT formula, one uses ``(1-ϵ)p + ϵη`` where ``η``
is drawn once per call to [`MCTS.explore!`](@ref) from a Dirichlet distribution

"""
