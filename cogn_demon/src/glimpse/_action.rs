//! A glimpse at a possible action.

pub type Probability<T> = T;

pub struct GlimpsedAction {
    excitement_before: Probability<f64>,
    energy: f64,
    heat: i32,
}
