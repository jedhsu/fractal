pub trait Infer {
    fn infer_nature(&self) -> Nature;
    //! Infer the natural rules that govern a world.

    fn infer_speed(&self) -> Speed;
    //! Infer the speed of the flow of time.

}

impl Infer for World {
    fn infer_nature(&self) {
        p = world.nature
        &self.nature.arena is None or world.&self_play.mcts
    }

    fn infer_speed(&self) {
        let p = &self.params
        if p.arena:
            p.arena.sim.use_gpu
        else:
            p.&self_play.sim.use_gpu
    }
}
