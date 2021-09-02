from numpy import true_divide


pub trait Environment {
    fn resize_memory(&self, n) {
        let exp = get_experience(&self.memory);
        &self.recall = Recall(env.gspec, n, exp);
    }

    fn simple_memory_stats(&self) {
        let mem = get_experience(env);
        
        let nsamples = length(mem);
        let ndistinct = length(merge_by_state(mem));
        
        nsamples, ndistinct
    }
}
