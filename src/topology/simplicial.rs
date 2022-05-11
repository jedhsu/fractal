/// The simplicial set defines the indexing mechanism of the n-simplex.
///
pub trait SimplicialSet<N>: Vec<HashSet<KM>>
where
    KM: KMorphism<K>,
{
}

/// Not sure if this framing is enough.

pub trait KMorphism<K> {
    /// The K-1 face.
    fn face(
        &self,
        idx: usize,
    ) -> Face;

    /// Defines all paths that lead to k+1 invariance.
    fn degeneracies(&self) {}
}
