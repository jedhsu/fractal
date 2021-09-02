
fn glimpsed(flow: &Flow) {
    piece = min(tr.params.loss_computation_batch_size, num_samples(tr))
    pieces = Flux.Data.DataLoader(tr.data; batchsize, partial=true)
#   reports = map(batches) do batch
#     batch = Network.convert_input_tuple(tr.network, batch)
#     return learning_status(tr, batch)
#   end
#   ws = <sum(batch.W) for batch in batches>
#   return Glimpsed(reports, ws)


pub struct Glimpsed(
    Evolved,
):
    fn evolve(&self):
        status = Evolved(tr)
        num_samples = sum(e.n for e in tr.samples)
        num_boards = length(merge_by_state(tr.samples))
        Wtot = sum(data_weights(tr))
        return Report.Samples(
            num_samples,
            num_boards,
            Wtot,
            status,
        )
