//! A samples collection is represented on the learning side as a (W, X, A, P, V)
//! named-tuple.
//!
//! Each component is a `Float32` tensor whose last dimension corresponds
//! to the sample index.
//!
//! Writing `n` the number of samples and `a` the total
//! number of actions:
//!
//! Note that the weight of a sample is computed as an increasing
//! function of its `n` field.



pub struct Observeds {
    architecture: Architecture,
    //! W (size 1×n) contains the samples weights

    history: History,
    //! X (size …×n) contains the board representations
    
    possibility: Possibility,
    //! A (size a×n) contains the action masks (values are either 0 or 1)

    shadow: Shadow,
    //! Sequence of whispers form a shadow, which is what "influences the mind".
    //!
    //! P (size a×n) contains the recorded MCTS policies

    //! path: Energy
    //! V (size 1×n) contains the recorded values
}
