//! A stream of consciuosness of the mind.

//! TODO where does this go
pub type Odyssey = Iterator<Thought>;

impl Odyssey {
    fn new() -> Odyssey:
        let batchsize = min(
            params.batch_size,
            length(W),
        )

        let batches = Flux.Data.DataLoader(
            data,
            batchsize,
            partial=false,
            shuffle=true,
        )

        map( batches, b)
}
