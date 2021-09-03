//! A fractum is a quantum extended with a spectrum.
//!
//! The name comes from the self-referential nature that this creates.

pub struct Fractum {
    position: Position,
    quantum: Quantum,
    spectrum: Spectrum,
}

impl Hash for Fractum {
    // fn __hash__(&self) -> int:
    //     return hash(&self.ident)
}
