//! Evaluate a single neural network for a one-player game.

pub trait Evaluate {
    fn evaluate(&self) -> Evaluated;
}

impl Evaluate for Pondering {
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

//# Single-player Games

//- `rewards` is the sequence of rewards collected by the evaluated player
//- `baseline_rewards` is the sequence of rewards collected by the baseline player
//- `avgr` is equal to `mean(rewards) - mean(baseline_rewards)`

//pub trait Evaluate {
//    fn evaluate(&self) {}
//    //! Evaluate a single brain for a unicameral mind.
//}

//impl Evaluate for Mind (
//}
