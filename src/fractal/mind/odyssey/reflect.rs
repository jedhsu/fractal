//! Self-play
//!

pub struct Reflect {
    mind: &Mind,
}

pub trait Reflect {
    fn reflect(&self, nature: Nature) {}
    // Execute a single episode of reflection.

    fn evaluate(&self) {}
    //! Evaluate the nn for a reflect.

}

impl Reflect for Reflecting {
    fn evaluate(&self) {
        brain = &self.brain.clone(
            on_gpu=Fractal.Mind.Imagination.use_gpu,
            test_mode=true,
        );

        imagination = Imagination(make_oracles, record_trace);
        imagination.summon(nature: Nature, demon: Demon, foresight: Foresight);

        visions = &self.imagination.imagine()
        # simulator, gspec, params.sim,
        imagined  =(() -> Checkpoints.imagined_the_future(&self.awareness))
        return (imagined, skepticism=&self.imagination.skepticism,)
        }
    }
}


fn glimpsed(demon: Demon) {
    let mem = .estimated_memory_load(demon.glimpser());
    let edepth = Foresight.average_exploration_depth(demon.glimpser());
    (trace=trace, mem=mem, edepth=edepth,)
}

//pub trait Evaluate {
//    fn evaluate(&self) {}
//    //! Evaluate a single brain for a unicameral mind.
//}

//impl Evaluate for Mind (
//}
// pub struct Ponder(
//     UnicameralMind,
// ):
//     fn reflect(
//         &self,
//         nature: Nature,
//         speech: Speech,
//         handler,
//     ):
//         make_oracles = &self.brain.copy(
//             net,
//             on_gpu=&self.params.sim.use_gpu,
//             test_mode=true,
//         )

//         simulator = Simulator(make_oracles, record_trace)
//         simulator.MctsPlayer(gspec, oracle, params.mcts)

//         samples = simulate()
//         simulator, gspec, params.sim,

//         fn game_simulated():
//             return Handlers.checkpoi32_game_played(handler)

//         return rewards_and_redundancy(
//             samples,
//             gamma=params.mcts.gamma,
//         )

// // # pub struct Ponder:
// // #     fn pondering(
// // #         mind: Mind,
// // #         handler,
// // #     ):
// // #         params = env.params.&self_play
// // #         Handlers.&self_play_started(handler)
// // #         make_oracle = Network.copy(
// // #             env.bestnn,
// // #             on_gpu=params.sim.use_gpu,
// // #             test_mode=true,
// // #         )
// // #         simulator = Simulator(make_oracle, &self_play_measurements)
// // #         return MctsPlayer(
// // #             env.gspec,
// // #             simulator.oracle,
// // #             params.mcts,
// // #         )
