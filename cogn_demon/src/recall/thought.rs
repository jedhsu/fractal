//! A stream of consciuosness of the mind.

pub type Odyssey = Iterator<Thought>;

impl Odyssey {
    fn new() -> Odyssey:
        batchsize = min(
            params.batch_size,
            length(W),
        )
        batches = Flux.Data.DataLoader(
            data,
            batchsize,
            partial=false,
            shuffle=true,
        )
        return map(
            batches,
            b,
        )
}
