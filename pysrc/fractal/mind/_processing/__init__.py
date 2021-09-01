
sample_state_type(::Type{<:TrainingSample{S}}) where S = S

"""
    MemoryBuffer(game_spec, size, experience=<>)

A circular buffer to hold memory samples.
"""

function augment_with_symmetries(gspec, samples)
  symsamples = <apply_symmetry(gspec, s, sym)
    for s in samples for sym in GI.symmetries(gspec, s.s)>
  return <samples ; symsamples>
end