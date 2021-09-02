
// sample_state_type(::Type{<:TrainingSample{S}}) where S = S

//! A circular buffer to hold memory samples.
//!
//! MemoryBuffer(game_spec, size, experience=<>)

fn augment_with_symmetries(nature: Nature, interpretations: Interpretation) {
    symsamples = <apply_symmetry(gspec, s, sym);
    for s in samples for sym in GI.symmetries(gspec, s.s)> {
        return <samples ; symsamples>
    }
}
