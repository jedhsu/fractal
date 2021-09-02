pub struct Reflection {
    glimpse: Glimpse,
    imagination: Imagination,
    // update_threshold: f64,
}


//! During &self-play, early board positions are possibly encountered many
//! times across several games.
//!
//! The corresponding samples can be merged together and given a weight ``W``
//! that is a nondecreasing function of the number ``n`` of merged samples:
//!
//! `CONSTANT_WEIGHT`: ``W(n) = 1`
//! `LOG_WEIGHT`: ``W(n) = \\log_2(n) + 1`
//! `LINEAR_WEIGHT`: ``W(n) = n``

pub enum SamplesWeighingPolicy {
    Constant,
    Linear,
    Logarithmic,
}
