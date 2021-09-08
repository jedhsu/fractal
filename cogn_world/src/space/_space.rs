//! The space defined by the world's geometry.
//!
//! There is one struct for each type of space, similar to how
//! the Iterator is implemented in Rust.

use serde::*
use std::fmt;

// pub struct Placement(
//     tuple<i32, ...>,
// ):
//     pass


// pub struct Space(
//     Tensor,
//     Mapping<tuple<i32, ...>, Position>,
//     Collection<Position>,
// ):
//     positions: set<Position>

//     fn __len__(&self) -> i32:
//         return len(&self.positions)

//     fn __getitem__(
//         &self,
//         position: Sequence<i32>,
//     ) -> Position:
//         return Position(position)

pub struct Space<N, D> {
    shape: Option<N>,
    datatype: Option<D>,
    seed: Option<i32>,
}


trait Seed<N, D> where N: Datatype {
    type N;
    type D;

    fn contains(&self, _: &Self::D) -> bool;
    fn seed(&self, _: &Self::D) -> N;
    fn sample(&self) -> D;
}


impl Serialize for Space {
}

// trait Tuple2<A, B>: Space where A: Space, B: Space {
// }
