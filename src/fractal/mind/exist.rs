//! Step process for the flow of time.

pub trait Flow<T> where T: Time {
    fn flow(&self):
        while &self.itc < &self.params.num_iters:
            &self.handle.iteration_started(handler)
            resize_memory!(env, env.params.mem_buffer_size<env.itc>)
            sprep, spperfs = Report.@timed &self_play_step!(env, handler)
            mrep, mperfs = Report.@timed memory_report(env, handler)
            lrep, lperfs = Report.@timed learning_step!(env, handler)
            rep = Observed.construct(Glimpsed(), Recalled(), Evolved(),)
            env.itc += 1
            &self.handle.iteration_finished(handler, rep)
        &self.handle.training_finished(handler)
}

impl Flow<T> for Realizing where T: Time {
    fn flow(&self):
        while &self.itc < &self.params.num_iters:
            &self.handle.iteration_started(handler)
            resize_memory!(env, env.params.mem_buffer_size<env.itc>)
            sprep, spperfs = Report.@timed &self_play_step!(env, handler)
            mrep, mperfs = Report.@timed memory_report(env, handler)
            lrep, lperfs = Report.@timed learning_step!(env, handler)
            rep = Observed.construct(Glimpsed(), Recalled(), Evolved(),)
            env.itc += 1
            &self.handle.iteration_finished(handler, rep)
        &self.handle.training_finished(handler)
}
