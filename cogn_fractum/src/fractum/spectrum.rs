//! Defines the probability distribution - a spectrum - of
//! future states for a quantum.
//!
//! Note that a change in quantum state can either be movement
//! (change in energy) or transfer (change in energy).

pub type Probability = f64;

// TODO distrubiton type
pub trait Spectrum<T>
where
    T: Map<QuantumState, Probability>,
{
}
