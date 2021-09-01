pub trait Experience {
    fn experience(&self);
}

impl Experience for Processing {
    fn experience(
        &self,
        recall: Recall,
        decay: DecayFactor,
    ) {
        n = len(trace);
        wr = 0;

        for i in range(1, n) {
            wr = gamma * wr + trace.rewards<i>;
            places = recall.states<i>;
            spectra = recall.spectra<i>;
            is_bright = GlobalInterpreter.white_playing(GlobalInterpreter.init(mem.gspec, s));
            z = wp ? wr : -wr;
            t = f64(n - i + 1);
            push!(mem.buf, TrainingSample(s, π, z, t, 1),);
        }
        self.cur_batch_size += n;
    }
}
