pub trait Integrate {
    // TODO are these the same results?
    //
    fn synthesize(&self) {}
    // Combine.

    fn integrate(&self) {}
    // Combine by state.
}

impl Integrate for Glimpse {
    fn synthesize(&self) {
      s = &self<1>.s

      let policy = mean(e.policy for e in samples)
      let z = mean(e.z for e in samples)
      let n = sum(e.n for e in samples)
      let t = mean(e.t for e in samples)
      
      eltype(samples)(s, π, z, t, n)
    }

    fn integrate(&self) {
        let Sample = eltype(samples)
        State = sample_state_type(Sample)
        dict = Dict{State, Vector{Sample}}()
        sizehi32!(dict, length(samples))

        for s in samples:
          if haskey(dict, s.s):
            push!(dict<s.s>, s)
        else:
            dict<s.s> = <s>

        return <merge_samples(ss) for ss in values(dict)>
    }
}
