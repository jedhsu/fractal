
evolve = Evolve(
    use_gpu=False,
    samples_weighing_policy=LOG_WEIGHT,
    l2_regularization=1e-4,
    optimiser=CyclicNesterov(
        lr_base=1e-3,
        lr_high=1e-2,
        lr_low=1e-3,
        momentum_high=0.9,
        momentum_low=0.8,
    ),
    batch_size=32,
    loss_computation_batch_size=2048,
    nonvalidity_penalty=1.0,
    min_checkpoints_per_epoch=0,
    max_batches_per_checkpoint=5_000,
    num_checkpoints=1,
)
