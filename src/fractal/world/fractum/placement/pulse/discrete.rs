//! A coarse clock represents step function schedules.
//!
//! StepSchedule(;start, change_at, values)
//!
//! Return a schedule that has initial value `start`. For all `i`, the schedule
//! takes value `values<i>` at step `change_at<i>`.

pub struct Coarsely<R> {
    start: R,
    xs: Vec<i32>,
    ys: Vec<R>,
}

impl Coarsely {
    fn new(start: R, xs: Vec<i32>, ys: Vec<R>) {
        assert_eq!(xs.len(), ys.len());
        Coarsely { start, xs, ys }
    }
}

// StepSchedule(; start, change_at, values) =
//   StepSchedule{typeof(start)}(start, change_at, values)

// function Base.getindex(s::StepSchedule, i::Int)
//    idx = findlast(x -> x <= i, s.xs)
//    isnothing(idx) && (return s.start)
//    return s.ys<idx>
// end

