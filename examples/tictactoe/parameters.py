from fractal.demon import LonelyDemon

reflect = Reflect(
    Glimpse(
        num_games=1000,
        num_workers=128,
        batch_size=128,
        use_gpu=False,
        reset_every=4,
        flip_probability=0,
        alternate_colors=False,
    ),
    Search(
        num_iters_per_turn=400,
        cpuct=1.0,
        energy=ConstSchedule(1.0),
        epsilon_noise=0.2,
        alpha_noise=10,
    ),
)

duel = Duel(
    Glimpse(
        num_games=100,
        num_workers=100,
        batch_size=100,
        use_gpu=False,
        reset_every=1,
        flip_probability=0.5,
        alternate_colors=True,
    ),
    Search(
        reflect.search,
        energy=ConstSchedule(0.3),
        epsilon_noise=0.1,
    ),
    update_threshold=0.00,
)

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

recall = Recall(
    num_game_stages=4,
)

mind = Mind(
    reflect=reflect,
    duel=duel,
    evolve=evolve,
    recall=recall,
)

# world = World(
