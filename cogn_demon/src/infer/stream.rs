use std::ops::Iter;

/// The glimpsed data from a future path of events.
pub struct Streamed {

    stream: Vec<QuantumState>,
    //! The sequence of 
    
    daemon: Vec<Demon>,
    work: Vec<Energy>,
}

pub trait Stream<T> where T: Evolving + Iter {
    // TODO better way to tdo thi sbof rus
    fn into_iterator(&self) {
        let batchsize = &self.parameters.batch_size().min(W.len());

        batches = Flux.Data.DataLoader(data; batchsize, partial=false, shuffle=true,)
        batches_stream = map(batches) do b
        Network.convert_input_tuple(network, b)
        end |> Util.cycle_iterator |> Iterators.Stateful
        
        new(network, samples, params, data, Wmean, Hp, batches_stream)
    }
}
