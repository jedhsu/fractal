from typing import Sequence


class Initialize(
    Evolving,
):
    def initialize(
        cls,
        nature: Nature,
        brain: Brain,
        observeds: Sequence[Observed],
        params: Parameters,
        is_testing: bool = false,
    ):
        if params.use_position_averaging:
            samples = observeds.merge_by_state()

        data = convert_samples(gspec, params.samples_weighing_policy, samples)
        brain = brain.clone(
            on_gpu=params.use_gpu,
            is_testing=is_testing,
        )
        W, X, A, P, V = data
        Wmean = mean(W)
        Hp = entropy_wmean(P, W)
