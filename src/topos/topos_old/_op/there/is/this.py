
"""
    current_state(game::AbstractGameEnv)

Return the game state.

!!! warn

    The state returned by this function may be stored (e.g. in the MCTS tree) and must
    therefore either be fresh or persistent. If in doubt, you should make a copy.

"""
function current_state end

# TODO: maybe MCTS should make the copy itself. The performance cost should not be great
# and it would probably avoid people a lot of pain.
