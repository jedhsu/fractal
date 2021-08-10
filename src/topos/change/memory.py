"""

    History

Parameters governing the analysis of the memory buffer
(for debugging and profiling purposes).

"""


class History:
    num_game_stages: int


"""

The memory analysis consists in partitioning the memory buffer in
`num_game_stages` parts of equal size, according to the number of
remaining moves until the end of the game for each sample. Then,
the quality of the predictions of the current neural network is
evaluated on each subset (see [`Report.Memory`](@ref)).

This is useful to get an idea of how the neural network performance
varies depending on the game stage (typically, good value estimates for
endgame board positions are available earlier in the training process
than good values for middlegame positions).
"""
