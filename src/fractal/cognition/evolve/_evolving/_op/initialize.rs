trait Initialize {}

impl Initialize for Evolving {
    fn initialize(
        &self,
        nature: Nature,
        brain: Brain,
        observeds: Sequence<Observed>,
        params: Parameters,
        is_testing: bool = false,
    ):
        if params.use_position_averaging {
            let samples = observeds.merge_by_state()
        }

        let data = convert_samples(nature, params.samples_weighing_policy, samples)
        let brain = brain.clone(
            on_gpu=params.use_gpu,
            is_testing=is_testing,
        )
        W, X, A, P, V = data
        Wmean = mean(W)
        Hp = entropy_wmean(P, W)
}
