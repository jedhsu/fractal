//! A possible action of a quantum.
//!
//! A quantum action is either a
//! * motion to a new position,
//! * change to a new state,
//!
//! potentially conditional on an action.

pub struct QuantumAction {
    condition: Option<Action>,
    probability: QuantumProbability,
}
