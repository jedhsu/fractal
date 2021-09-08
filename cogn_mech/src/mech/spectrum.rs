//! A spectrum defines the probability distribution of
//! future states for a datum.
//!
//! Note that a change in quantum state can either be movement
//! (change in energy) or transfer (change in energy).

pub type Probability = f64;

pub trait Spectrum<Datum, Datum> {
    fn probability(datum: Datum);
}
