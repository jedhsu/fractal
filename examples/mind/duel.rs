
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
