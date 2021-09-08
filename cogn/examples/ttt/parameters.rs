
// TODO need to build this with builder pattern
//
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
