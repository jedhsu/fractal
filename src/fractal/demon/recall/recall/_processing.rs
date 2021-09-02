//! Memory buffer.

pub type Complexity = i32;

pub struct Processing {
    nature: Nature,

    ring: RingBuffer<Observation>,

    complexity: Complexity,
    // Batch size.
}

