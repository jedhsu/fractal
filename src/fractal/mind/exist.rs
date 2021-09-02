//! Step process for the flow of time.

pub trait Flow<T> where T: Time {
    fn flow(&self);
}

impl Flow<T> for Realizing where T: Time {
    fn flow(&self) {
        while &self.itc < &self.params.num_iters {
            &self.handle.iteration_started(handler);
            resize_memory!(env, env.params.mem_buffer_size<env.itc>);
            
            // 1 - Glimpse
            let sprep, spperfs = &self.ponder(&self.realizing, &self.world.clock);

            // 2 - Analyze
            let mrep, mperfs = Report.@timed memory_report(env, handler);

            // 3 - Evolve
            let lrep, lperfs = Report.@timed learning_step!(env, handler);
            
            // let sprep, spperfs = Report.@timed &self_play_step!(env, handler);
            // let mrep, mperfs = Report.@timed memory_report(env, handler);
            // let lrep, lperfs = Report.@timed learning_step!(env, handler);

            let rep = Observed.construct(Glimpsed(), Recalled(), Evolved(),);
            let env.iteration_count += 1;

            &self.handle.iteration_finished(handler, rep);
        }
}
