//! Describes how to measure the value of a state.

pub struct Inferred<T: State>  {
    distribution: set<PlacementAnalysis>,
    //! The probability distribution on `GI.available_actions(GI.init(gspec, state))`

    expected: f64,
    //! A scalar estimating a value metric.
}

// pub struct Inferred {
//     state: T::&State, // TODO clarify this syntax, but it's right approach
// }

pub trait Infer<T> where T: State {
    pub type Inferred;
   
    /// ... doenst fit
    fn total_inferred(&self) -> usize {
        return sum(s.total for s in b.stats)
    }
}

