pub trait Flow {
    fn tick(&self, realizing: Realizing);
    fn evaluate(&self, realizing: Realizing) -> Played;
    //! Compare two versions of a neural network (params::ArenaParams)
    //!
    //! Works for both two-player and single-player games.

    fn reset(&self);
}

impl Flow for Duel {
    fn tick(&self, realizing: Realizing) {
        if world.is_it_dawn(game) {
            &self.white.tick(realizing);
        } else {
            &self.black.tick(realizing);
        }
    }

    fn evaluate(&self, clock: Clock) {
        legend = "Most recent NN versus best NN so far"

        if Flow.two_players(gspec) {
            let (rewards_c, red), t = pit_networks(gspec, contender, baseline, params, handler,)
                avgr = mean(rewards_c)
                rewards_b = nothing;
        } else {
            let (rewards_c, red_c), tc = contender.evaluate(nature, params, handler,);
            let (rewards_b, red_b), tb = baseline.evaluate(nature, params, handler,);

            let avgr = mean(rewards_c) - mean(rewards_b);
            let red = mean(<red_c, red_b>);
            let t = tc + tb;

            Dueled(legend, avgr, red, rewards_c, rewards_b, t,);
    }
    
    fn reset(&self) {
        &self.white.reset() & self.black.reset()
    }
    
}
