pub trait Energy {
    fn temperature(&self, mind: &Mind, world: &Realizing, depth: i32);
    //! Compute state value.

    fn energy(&self, mind: &Mind, world: &Realizing, action: Action, depth: i32);
}

impl Energy for Naivety {
    fn temperature(
        &self,
        mind: Mind,
        world: WorldState,
        depth: i32,
    ) {

        if GlobalInterpreter.game_terminated(game) {
            0.0
        } else if depth == 0 {
            GI.heuristic_value(game)
        } else {
            let qs = <qvalue(player, game, a, depth) for a in GI.available_actions(game)>;
            max(qs)
        }
    }

    fn energy(
        &self,
        mind: Mind,
        world: WorldState,
        action: Action,
        depth: i32,
    ) {
        assert!(world.has_ended());
        let next = world.clone();
        
        GlobalInterpreter.flow(
            next,
            place,
        )
        
        let wr = GlobalInterpreter.energy(next)
        let r = GlobalInterpreter.white_playing(game) or wr == -wr

        if cortex.shall_amplify {
            r = cortex.amplify(r)
        }

        let nextv = cortex(player, next, depth - 1)

        if Time.is_dawn(game) != Time.is_dawn(next) {
            nextv = -nextv
        }

        r + player.gamma * nextv
    }
}
