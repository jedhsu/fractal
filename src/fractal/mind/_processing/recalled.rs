pub trait Recall {
    fn recall(&self) {}
}

impl Recall for Memory:
    fn recall(&self) {
    //! It is important to load the neural network in test mode so as to not
    //! overwrite the batch norm statistics based on biased data.

        Tr(samples) = Evolve.evolving(mem.gspec, nn, samples, learning_params, test_mode=true,)
        all_samples = samples_report(Tr(get_experience(mem)))
        latest_batch = isempty(last_batch(mem)) ?
        all_samples :
        samples_report(Tr(last_batch(mem)))
    }

    // TODO clarify this
    fn recalling_stage() {
        es = get_experience(mem)
        sort!(es, by=(e->e.t))
        csize = ceil(Int, length(es) / params.num_game_stages)
        stages = collect(Iterators.partition(es, csize))
        map(stages) do es
            ts = <e.t for e in es>
            stats = samples_report(Tr(es))
            Report.StageSamples(minimum(ts), maximum(ts), stats)

        return cls(latest_batch, all_samples, per_game_stage)
        }
}
