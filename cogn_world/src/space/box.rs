//! A possibly unbounded box in R^n.

pub struct Box<I: Interval<f32, f32>, S: Shape, D: Datatype> {
    interval: I<f32, f32>,
    shape: S,
    datatype: D,
}

pub enum BoundingDirection {
    Below,
    Above,
    Both,
}

impl<I: Interval, S: Shape, D: Datatype> Box<I, N, D> {
    pub fn new<I, S, D>(interval: I, shape: S, datatype: D) -> Self {
        Box {
            interval,
            shape,
            datatype,
        }
    }

    fn is_bounded(&self, dir: BoundingDirection);
}
