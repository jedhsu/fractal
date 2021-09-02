pub trait Process {
    fn process(&&self);
}

impl Process for Memory {
    fn process(
        &self,
    ) {
        let mut n: i32 = len(trace);
        let mut wr: i32 = 0;

        for i in 1..n {
            let wr = caution * wr + trace.rewards<i>;
            let places = recall.states<i>;
            let spectra = recall.spectra<i>;

            is_bright = GlobalInterpreter.white_playing(GlobalInterpreter.init(mem.gspec, s));
            z = wp ? wr : -wr;
            t = f64(n - i + 1);
            push!(mem.buf, TrainingSample(s, π, z, t, 1),);
        }
        &self.cur_batch_size += n;
    }
}
