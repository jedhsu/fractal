//! *Reset*

pub trait Wipe {
    fn wipe(&self);
}

impl Wipe for BicameralMind {
    fn wipe(&self) {
        &self.white.reset() & self.black.reset()
    }
}