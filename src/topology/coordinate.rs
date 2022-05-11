pub trait Coordinate<Op>
where
    Op: Operator<X, Y>,
    X: Real<N>,
    Y: Space,
    N: Level,
{
}

pub mod tests {
    fn coordinate() {}
}
