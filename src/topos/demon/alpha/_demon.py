"""

    *Alpha Demon*

  Create an AlphaZero player from the current [training environment](@ref environment).

  Note that the returned player may be slow as it does not batch MCTS requests.

"""

from typing import Optional

from alpha0.environment import Environment
from alpha0.parameters import MonteCarloTreeSearch


def AlphaDemon(
    env: Environment,
    mcts_params: MonteCarloTreeSearchParameters,
    gpu: Optional = None,
    timeout: float = 2.0,
):
    if not mcts_params:
        mcts_params = MonteCarloTreeSearchParameters.guess(environment)

    if not gpu:
        gpu = GraphicalProcessingUnit.guess(gpu)

    net = Network.copy(
        env.optimalnet,
        on_gpu=gpu,
        test_mode=true,
    )
    return MctsPlayer(
        env.gspec,
        net,
        mcts_params,
        timeout=timeout,
    )
