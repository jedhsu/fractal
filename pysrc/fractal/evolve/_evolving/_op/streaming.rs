from typing import Iterator

from .._evolving import Evolving

class Streaming(Evolving, Iterator[Batch],):
    fn batches_iterator(&self) {
        let batchsize = min(params.batch_size, length(W))
        batches = Flux.Data.DataLoader(data; batchsize, partial=false, shuffle=true,)
        batches_stream = map(batches) do b
        Network.convert_input_tuple(network, b)
        end |> Util.cycle_iterator |> Iterators.Stateful
        return new(network, samples, params, data, Wmean, Hp, batches_stream)
    }
