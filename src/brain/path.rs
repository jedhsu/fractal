pub struct Vibration<X, Y>
where
    X: Neuron,
    Y: Neuron,
{
    left: X,
    right: Y,
}

pub struct Path1<X, Y>
where
    X: i32,
    Y: i32,
{
    left: X,
    right: Y,
}

// pub trait PathOrient<Segment<N>>
// where
//     N: u32,
// {
// }
