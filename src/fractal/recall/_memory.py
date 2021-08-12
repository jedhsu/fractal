class Memory(
    Gestalt,
    State,
):
    physics: Physics
    ring: TrainingSample[State]
    cur_batch_size: int
