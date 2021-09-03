use std::hash::Hash;



pub trait Quantum<E> where E: Sized + Identity + Energy + Action  {
    //! A Quantum is an atomic Datum.
    //!
    //! It is analagous to the quark, but not exactly. For instance, note that
    //! could serve as "direct" atoms of World, while quarks are only defined on
    //! the three traditional dimensions of space.

    
    /// A quantum in a flowing spacetime possesses state.
    

}

/// Note the nuance here of how Quantum was written as a trait, but the stateful part as a struct, and the identity defines on the stateful part. This feels importnat.

pub struct QuantumState {
    position: Position,
    //! Returns the spatial-only position vector of the quantum defined at the current time.
    
    energy: Energy,
    //! Returns the energy scalar of the quantum defined at the current time.
}

impl QuantumState {
    fn measured(&self) {&Self };
    //! Returns quantum state.

}

pub trait Identity {
    fn named(&self) -> u64;
    //! Returns a unique represetation of a quantum state. (TODO this can be generic)
}

pub trait Energy {
    //! An interface defining how to specify the domain - the total set of energy states.
    //!
    //! Needs to be framed as a rule...

    fn states(&self) -> Iter<&str> {};
}

//! A possible action of a quantum.
//!
//! A quantum action is either a
//! * motion to a new position,
//! * change to a new state,
//!

pub enum QuantumActed {
    // TODO define types?
    Movement<Position, Position>,
    Transfer<Energy, Energy>,
}

pub trait Action {
    //! Specifies the inferred chain of events
    //! (this will need to be worked out)

    type Causes = Vec<QuantumAction>;
    // Associated type holding the set of causes. This needs to be generalized from quantum action
    // in practice.

pub struct QuantumAction {
    condition: Option<Action>,
    probability: QuantumProbability,
}

pub trait ActionDomain {
    fn states(&self) -> Iter<&self> {};
}

// TODO clarify triat implementations
// TODO clarify how to work with hashes in rust

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
