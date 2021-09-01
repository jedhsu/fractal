"""
Evaluate
========

Evaluate a single neural network for a one-player game.

"""

from fractal.world import Nature
from fractal.brain import Brain
from fractal import Fractal

from .._mind import Mind


class Evaluate(
    Mind,
):
    @classmethod
    def thinking(
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
        # game_simulated=(() -> Handlers.checkpoint_game_played(handler))
        # return rewards_and_redundancy(samples, gamma=params.mcts.gamma,)
