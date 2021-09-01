//! A quantum is analagous to a physical particle.

use std::hash::Hash

from abc import ABCMeta

pub type QuantumState {}

pub struct Quantum {
    position: Position
    state: QuantumState
}

impl Hash for Quantum {
    fn hash<H: Hasher<(&self) -> u64:
        return hash {
            (
                self.__class__,
                self.position,
                self.state,
            )
        }
}
// @dataclass
//  Quantum(
//     Hashable,
//     metaclass=ABCMeta,
// ):

