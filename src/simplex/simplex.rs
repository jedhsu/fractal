pub struct Simplex0 = &str

pub struct ȭ = &str

pub struct Simplex<N> {
}

/// A triangulizable space is homeomorphic to the simplicial complex.
pub trait Triangulizable {
    pub type = TopologicalSimplex;

    /// Consider a simplex, the object.
    ///
    /// The simplex closes if it is an invariant metric state. This definition implies that it
    /// holds the logic of a minimal predicate on that closure. Precisely, this is the topological space in which it resides.
    /// 
    /// A closed simplex is equivalent with its N+1 open simplex.
    ///
    /// This likely is a local equivalence, and does not imply anything else.
    fn closed(&self) -> bool { }

}

/// The 0-simplex is the arrow / perhaps cold-string.
///
/// Philosophically, the nature of a quanta might arise at this level, but does not become well-defined until after the homotopy-level that defines it.

pub struct Simplex0 {
    left: Simplex1,
}

/// The 1-simplex is the point, the closed 0-simplex.

pub struct Simplex1 {
    left: Simplex0,
    right: Simplex0,
}


pub trait Simplex2 {
    left: Simplex1,
    right: Simplex1,
}

pub trait Simplex3 {
}
