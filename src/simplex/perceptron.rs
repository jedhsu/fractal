
/// The L1-element.
pub trait Perceptron<K>: SimplicialCell<K> where K: CategoryLevel {
    fn parameters(&self) {};
}
