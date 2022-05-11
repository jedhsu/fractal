pub struct SimplicialCell<K, N, S>
where
    S: Space,
{
    level: K,
}

pub trait Shape {
    fn project(
        &self,
        element: Element<Space>,
    );
}
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
