/// From the frame of reference of the face, it is closed.
///
/// The code for frame of reference should be embedded into all types.

pub trait Face<K> {
    fn closed();
}

pub trait Face<K, K-1> {
    fn closed();
}
