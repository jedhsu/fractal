//! Loss metrics.

pub struct Optimized {
    total: f32,
    cross_entropy: f32,
    average_mse: f32,
    regularization: f32,
    invalid: f32,
}