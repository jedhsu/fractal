/// The geometric realization of K.
pub trait Polyhedron<K> {
    fn form(&self, K: Level);
        /// spatiallyglue
    }
}
pub struct Vertex<N> {
    name: &str,
    dimensions: N,
}

/// Not sure how free to make these operations yet, haven't studied their side-effects.
pub trait Polyhedra {
    /// Expand a n-vertex into a n-face.
    fn expand(&self);

    /// Collapse an N-face into a n-vertex.
    fn collapse(&self);
}
