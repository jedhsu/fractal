from numpy import true_divide


class Environment:
    def resize_memory(self, n):
        exp = get_experience(self.memory)
        self.recall = Recall(env.gspec, n, exp)

    def simple_memory_stats(self):
        mem = get_experience(env)
        nsamples = length(mem)
        ndistinct = length(merge_by_state(mem))
        return nsamples, ndistinct
