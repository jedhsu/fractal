"""

    *Process*

  Collect samples out of a game trace and add them to the memory buffer.

  Here, `gamma` is the reward discount factor.

"""


class Process(
    Memory,
):
    def processed(
        self,
        recall: Recall,
        decay: DecayFactor,
    ):
        n = len(trace)
        wr = 0

        for i in range(1, n):
            wr = gamma * wr + trace.rewards[i]
            places = recall.states[i]
            spectra = recall.spectra[i]
            is_bright = GlobalInterpreter.white_playing(GlobalInterpreter.init(mem.gspec, s))
            z = wp ? wr : -wr
            t = float(n - i + 1)
            push!(mem.buf, TrainingSample(s, π, z, t, 1),)
        self.cur_batch_size += n
