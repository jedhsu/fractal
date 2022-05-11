pub struct Vertex<N> {
    name: &str,
    dimensions: N,
}

pub trait Polyhedra {
    /// Expand a n-vertex into a n-face.
    fn expand(&self);

    /// Collapse an N-face into a n-vertex.
    fn collapse(&self);
}
