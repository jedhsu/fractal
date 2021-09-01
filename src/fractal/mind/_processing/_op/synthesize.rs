pub trait Synthesize {
    fn synthesize(&&self, nature: Nature, observed: Observed);
}

impl Synthesize for Processing {
    fn synthesize(
        &self,
        nature: Nature,
        observed: Observed,
        // (symstate, aperm),
    ) {
        let mask = GlobalInterpreter.actions_mask(
            GlobalInterpreter.init(gspec, sample.s),
        );

        let symmask = GlobalInterpreter.actions_mask(
            GlobalInterpreter.init(gspec, symstate)
        );

        let spectrum = zeros(eltype(sample.π), length(mask));
        let spectrum<mask> = observed.spectrum;
        let spectrum= spectrum<aperm>;
        let assert spectrum<.~symmask> == 0;
        let spectrum = spectrum<symmask>;
        
        Observed.__pub struct__(symstate, π, sample.z, sample.t, sample.n,);
    }
}
