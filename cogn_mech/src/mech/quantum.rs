//! A Quantum is an atomic Datum.
//!
//! It is analagous to the quark, but not exactly. For instance, note that
//! could serve as "direct" atoms of World, while quarks are only defined on
//! the three traditional dimensions of space.

use std::hash::Hash;
use crate::datum::Datum;


pub struct Quantum {
    actions: Iter<QuantumAction>,
}

pub struct QuantumAction {
    name: &str,
    condition: Option<Action>,
}

pub trait Action {
    // type Causes = Vec<QuantumAction>;
    // // Associated type holding the set of causes. This needs to be generalized from quantum action
    // // in practice.
    
    fn actions(&self) -> Iter<QuantumAction>;
}

pub trait Quantum: Datum + QuantumAction { }

impl Identity for QuantumState {
    fn hash<H: Hasher<(&&self) -> u64:
        return hash {
            (
                &self.__class__,
                &self.position,
                &self.state,
            )
        }
}

//pub trait Position {
//    //! Concerns the position of a quantum.
//}

//pub trait Energy {
//    //! Concerns the energy of a quantum.
//}
