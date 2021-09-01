//! *Reset*

pub trait Reset {
    fn reset(&self);
}

impl Reset for Duel {
    fn reset(&self) {
        &self.white.reset() & self.black.reset()
    }
}

