
pub trait Flow<T> where T: Sized {};
//! Represents a function from
//! nonnegative integers to numbers of type `R`.
//!
//! Subtraits must implement the
//!
//!   `getindex(s::AbstractSchedule, i::Int)` operator.
//!
//! Remark - use the name Flow, rather than Path, to emphasize how it is in time.

