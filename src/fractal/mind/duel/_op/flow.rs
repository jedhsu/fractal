pub trait Flow {
    fn flow(&self, world: World, time: Time);
}

impl Flow for Duel {
    fn flow(
        &self,
        world: World,
        time: Time,
    ):
        if world.is_it_dawn(game):
            return &self.white.flow(
                spacetime,
                epoch,
            )
        else:
            return &self.black.flow(
                spacetime,
                epoch,
            )
}
