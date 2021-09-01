
pub trait Evaluate {
    fn evaluate(&self) {}
    //! Evaluate a single brain for a unicameral mind.
}

impl Evaluate for Mind (
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
