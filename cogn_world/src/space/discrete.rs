//! A discrete space.

use num_traits::Unsigned;
use crate::space::Space;
use rand::Rng;

pub struct Discrete<N: Unsigned> {
    size: N,
}

pub trait Discrete<A>: Space where A: Unsigned {
    type A;
}

impl<N> Space for Discrete<N> where N: Unsigned {
    fn sample(&self) -> N {
        self.
    }
    fn contains(&self) -> bool {}
}

impl Display for Space {
    fn fmt(&self, f: &mut fmt:Formatter) -> Result {
        write!(f, "{}", self.n)
    }
}

impl PartialEq for Space {
}
