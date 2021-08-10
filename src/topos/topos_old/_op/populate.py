class Populate:


def populate_arrays():
    if mask1 and mask2.isempty():
        return fill_and_evaluate(
            net1,
            batch1,
            fill_batches,
            batch_size=n,
        )
    elif mask2 and mask1.isempty():
        return fill_and_evaluate(
            net2,
            batch2,
            fill_batches,
            batch_size=n,
        )
    else:
        res1 = fill_and_evaluate(
            net1,
            batch1,
            fill_batches,
            batch_size=n,
        )
        res2 = fill_and_evaluate(
            net2,
            batch2,
            fill_batches,
            batch_size=n,
        )

        assert isinstance(res1) == isinstance(res2)
        res = similar(res1, n)
        res[mask1] = res1
        res[mask2] = res2
        return res
