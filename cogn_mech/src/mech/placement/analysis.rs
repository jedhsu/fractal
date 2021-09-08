//! Describes how to measure the value of a state.

pub struct Inferred {
    distribution: set<PlacementAnalysis>,
    expected_value: f64,
}

pub trait Infer<T> where T: State {
    pub type Inferred;
    
    fn total(&self):
        return sum(s.N for s in b.stats)
}

