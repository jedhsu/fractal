
pub struct Evolving {
    brain: Brain,
    placements: Vec<TrainingSample>,
    # data: NamedTuple # (W, X, A, P, V) tuple obtained after converting `samples`,
    Wmean: f32,
    Hp: f32,
    batches_stream: Iterator<Batch>,
}

impl Evolving {
    # end |> Util.cycle_iterator |> Iterators.Stateful
    return new(network, samples, params, data, Wmean, Hp, batches_stream,)
    }