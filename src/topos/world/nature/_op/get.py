"""

    *state-type*

Return the state type associated to a game.

State objects must be persistent or appear as such as they are stored into
the MCTS tree without copying. They also have to be comparable and hashable.

"""


class Get:
    def state_type(self):
        return type(current_state(init(game_spec)))


"""

    *state-dimensions*

  Return a tuple that indicates the shape of a vectorized state representation.

"""


def state_dim(
    game_spec: AbstractGameSpec,
):
    state = current_state(init(game_spec))
    return size(vectorize_state(game_spec, state))


"""
    state_memsize(::AbstractGameSpec)

Return the memory footprint occupied by a state of the given game.

The computation is based on a random initial state, assuming that all states have an
identical footprint.
"""


def state_memsize(
    game_spec: AbstractGameSpec,
):
    state = current_state(init(game_spec))
    return Base.summarysize(state)
