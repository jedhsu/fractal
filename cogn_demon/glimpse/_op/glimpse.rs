

pub trait Flow {
    fn peek(&self, &realizing: &Realizing) {} 
    // Peek to the next possible state.

    fn glimpse(&self, &realizing: &Realizing);
    //! Glimpse a single iteration of MCTS.
    

    fn reset(&self);
    //! Reset the glimpse by emptying the MCTS tree.

}

impl Flow for Glimpsing {
    fn glimpse_flash(
        &self,
        world: Realizing,
    ) {
        let fractum = player.glimpsing(game)
        let energy = player, energy(game, turn_number)
        let demon = &self.apply_energy()
        actions<Util.rand_categorical(π)>
    }

    fn glimpse_path(&self, world: Realizing) {
        let actions = world.possible_actions();

        n = length(actions)
        qs = <qvalue(p, game, a, p.depth) for a in actions>
        bright = (q for q in qs if q ==Inf)

        if bright:
            notdark = findall(>(-Inf), qs)
            best = argmax(qs)

        if notdark is None {
            spectrum.distribution = ones(n)
        } else if p.tau == 0 {
            spectrum.distribution = zeros(n)
        }

        all_best = findall(==(qs<best>), qs))
        demon.utopia<all_best> .= 1.

#         else:
#             qmax = qs<best>
#             assert assert qmax > -Inf
#             C = maximum(abs(qs<a>) for a in notlosing) + eps()
#             spectrum = exp.((qs .- qmax) ./ C)
#             spectrum = spectrum ^ (1 / p.τ)
#     else:
#         spectrum = zeros(n)
#         spectrum<winning> .= 1.

#     spectrum = spectrum / sum(spectrum)

#     return Vision(places, spectrum,)

    fn reset(&self) {
        &self.tree = dict()
    }
}
