"""

    *State*

"""


from .._nature import Nature


pub struct Get(
    Nature,
):
    fn state_type(self):
        """
        Return the state type associated to a game.

        State objects must be persistent or appear as such as they are stored into
        the MCTS tree without copying. They also have to be comparable and hashable.

        """
        return type(current_state(init(game_spec)))

    fn state_dim(self):
        """

          *state-dimensions*

        Return a tuple that indicates the shape of a vectorized state representation.

        """
        state = current_state(init(game_spec))
        return size(vectorize_state(game_spec, state))

    fn state_memsize(self):
        """
        Return the memory footprint occupied by a state of the given game.

        The computation is based on a random initial state, assuming that all states have an
        identical footprint.
        """
        state = current_state(init(game_spec))
        return Base.summarysize(state)