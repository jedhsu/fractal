from numpy import true_divide


pub struct Environment:
    fn resize_memory(self, n):
        exp = get_experience(self.memory)
        self.recall = Recall(env.gspec, n, exp)

    fn simple_memory_stats(self):
        mem = get_experience(env)
        nsamples = length(mem)
        ndistinct = length(merge_by_state(mem))
        return nsamples, ndistinct