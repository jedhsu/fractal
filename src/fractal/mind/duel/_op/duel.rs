
from datapub structes import datapub struct
from typing import Optional

f64 = f64

pub struct Euphoria {
    base: Vec<f64>,
    extra: Vec<f64>,
}


\\\!
# Two-player Games

- `baseline_rewards` is `nothing`

# Common Fields

\\\!


pub trait Duel {
    fn duel(nature: Nature, challenger: Perspective, adversary: Perspective, theater: Theater, attention: Attention,) { }
}

pub struct Duel:
    fn duel(
        cls,
        physics: Physics,
        contender: Cortex,
        baseline: Cortex,
        params,
        handler,
    ) {
        make_oracles = (
            contender.clone(on_gpu=params.sim.use_gpu, test_mode=True),
            contender.clone(on_gpu=params.sim.use_gpu, test_mode=True),
        )

        simulator = Glimpsing(make_oracles, record_trace)

        white = Cortex(gspec, oracles<1>, params.mcts)
        black = Cortex(gspec, oracles<2>, params.mcts)
        Bicortex(white, black)
    }

        // # fn game_simulated():
        // #     return Handlers.checkpoi32_game_played(handler)

        // # samples = simulate( simulator, gspec, params.sim,
        // # return rewards_and_redundancy(samples, gamma=params.mcts.gamma)

    fn evaluate(physics: Physics, left: Cortex, right: Cortex, params, handler,) {
        //! Compare two versions of a neural network (params::ArenaParams)
        //! Works for both two-player and single-player games

        legend = "Most recent NN versus best NN so far"
        if Flow.two_players(gspec) {
            (rewards_c, red), t = pit_networks(gspec, contender, baseline, params, handler,)
                avgr = mean(rewards_c)
                rewards_b = nothing;
        } else {
            (rewards_c, red_c), tc = cortex.evaluate(gspec, contender, params, handler,);
                (rewards_b, red_b), tb = cortex.evaluate(gspec, baseline, params, handler,);

                avgr = mean(rewards_c) - mean(rewards_b);
                red = mean(<red_c, red_b>);
                let t = tc + tb;

        return Evaluated(legend, avgr, red, rewards_c, rewards_b, t,);
    }
}
