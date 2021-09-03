pub trait Recall {
    fn recall(&self);
    //! It is important to load the neural network in test mode so as to not
    //! overwrite the batch norm statistics based on biased data.

    fn recalling_stage(&self) -> Memory;
}

impl Recall for Memory:
    fn recall(&self) {
        let Tr(samples) = Evolve.evolving(nature, brain, samples, evolution, test_mode=true,);

        let all_samples = samples_report(Tr(get_experience(mem)));
        let latest_batch = if last_batch(mem) is None {
            all_samples } else {
            samples_report(Tr(last_batch(mem)));
            }
    }

    fn recalling_stage() {
        let es = &self.recall_experience();
        sort!(es, by=(e->e.t))

        let csize = ceil(Int, length(es) / params.num_game_stages)
        let stages = collect(Iterators.partition(es, csize))

        map(stages) do es
            ts = <e.t for e in es>
            stats = samples_report(Tr(es))
            Report.StageSamples(minimum(ts), maximum(ts), stats)

        Memory {latest_batch, all_samples, per_game_stage}
    }
}
