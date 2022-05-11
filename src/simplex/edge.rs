pub trait Edge for SimplicialCell<K> {
    fn edges(&self) -> Vec<&SimplicialCell<K-1>>;
}
