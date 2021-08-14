"""

    *Recall*

"""


class Recall(
    Gestalt,
    State,
):
    physics: Physics
    ring: TrainingSample[State]
    cur_batch_size: int
