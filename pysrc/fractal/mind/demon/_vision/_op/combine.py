pub struct Combine:
    fn combine(self):
      s = self<1>.s
      π = mean(e.π for e in samples)
      z = mean(e.z for e in samples)
      n = sum(e.n for e in samples)
      t = mean(e.t for e in samples)
      return eltype(samples)(s, π, z, t, n)

    fn combine_by_state(self):
        Sample = eltype(samples)
        State = sample_state_type(Sample)
        dict = Dict{State, Vector{Sample}}()
        sizehint!(dict, length(samples))

        for s in samples:
          if haskey(dict, s.s):
            push!(dict<s.s>, s)
        else:
            dict<s.s> = <s>

        return <merge_samples(ss) for ss in values(dict)>