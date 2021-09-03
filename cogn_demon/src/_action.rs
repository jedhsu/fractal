//! A glimpse at a possible action.

pub type Probability<T> = T;

pub struct ActionPotential {
    excitement_before: Probability<f64>,
    reward: f64,
    frequency: i32,
}
