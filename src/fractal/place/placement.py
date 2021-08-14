from dataclasses import dataclass


@dataclass
class Place:
    placements: Vector[Placement]
    estimated_heat: f32


def place(
    spacetime: Spacetime,
    placing: Place,
):
    if placing in spacetime.tree:
        return (env.tree[state], false)
    else:
        (P, V) = env.oracle(state)
        info = init_state_info(P, V, env.prior_temperature)
        env.tree[state] = info
        return (info, true)
