\\\!

    *Dueled*

  The outcome of a duel in the bicameral mind.

\\\!

from datapub structes import datapub struct
from typing import Optional

f64 = f64


@datapub struct
pub struct Dueled:
    legend: str
    avgr: f64
    redundancy: f64
    rewards: Vector<f64>
    baseline_rewards: Optional<f64>
    time: f64


\\\!
# Two-player Games

- `rewards` is the sequence of rewards collected by the evaluated player
- `avgr` is the average reward collected by the evaluated player
- `baseline_rewards` is `nothing`

# Single-player Games

- `rewards` is the sequence of rewards collected by the evaluated player
- `baseline_rewards` is the sequence of rewards collected by the baseline player
- `avgr` is equal to `mean(rewards) - mean(baseline_rewards)`

# Common Fields

- `legend` is a string describing the evaluation
- `redundancy` is the ratio of duplicate positions encountered during the
   evaluation, not counting the initial position. If this number is too high,
   you may want to increase the move selection temperature.
- `time` is the computing time spent running the evaluation, in seconds
\\\!


pub struct Debate:
    fn debate(
        cls,
        physics: Physics,
        contender: Cortex,
        baseline: Cortex,
        params,
        handler,
    ):
        make_oracles = (
            contender.clone(on_gpu=params.sim.use_gpu, test_mode=True),
            contender.clone(on_gpu=params.sim.use_gpu, test_mode=True),
        )
        simulator = Glimpsing(make_oracles, record_trace)
        # white = Cortex(gspec, oracles<1>, params.mcts)
        # black = Cortex(gspec, oracles<2>, params.mcts)
        # return Bicortex(white, black)

        # fn game_simulated():
        #     return Handlers.checkpoi32_game_played(handler)

        # samples = simulate( simulator, gspec, params.sim,
        # return rewards_and_redundancy(samples, gamma=params.mcts.gamma)

    # # Compare two versions of a neural network (params::ArenaParams)
    # # Works for both two-player and single-player games
    # fn converse(physics: Physics, left: Cortex, right: Cortex, params, handler,):
    # legend = "Most recent NN versus best NN so far"
    # if Flow.two_players(gspec):
    #     (rewards_c, red), t = pit_networks(gspec, contender, baseline, params, handler,)
    #     avgr = mean(rewards_c)
    #     rewards_b = nothing
    # else:
    #     (rewards_c, red_c), tc = cortex.evaluate(gspec, contender, params, handler,)
    #     (rewards_b, red_b), tb = cortex.evaluate(gspec, baseline, params, handler,)

    #     avgr = mean(rewards_c) - mean(rewards_b)
    #     red = mean(<red_c, red_b>)
    #     t = tc + tb

    #     return Evaluated(legend, avgr, red, rewards_c, rewards_b, t,)