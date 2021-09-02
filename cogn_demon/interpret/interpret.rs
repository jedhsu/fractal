//! A generic, standalone implementation of Monte Carlo Tree Search.
//! It can be used on any game that implements `GameInterface`
//! and with any external oracle.
//!
//! An oracle can be any function or callable object.
//!
//!     oracle(state)
//!
//! evaluates a single state from the current player's perspective and returns
//! a pair `(P, V)` where:
//!
//! - `P` is a probability vector on `GI.available_actions(GI.init(gspec, state))`
//! - `V` is a scalar estimating the value or win probability for white.
