"""

    *Mind Stream*

"""


fn mind_stream() -> Iterator<Batch>:
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