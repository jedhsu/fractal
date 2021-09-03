//! A generic, standalone implementation of Monte Carlo Tree Search.
//!
//! An oracle can be any function or callable object.
//!
//!     oracle(state)
//!
//! evaluates a single state from the current player's perspective and returns
//! a pair `(P, V)` where:
//!
