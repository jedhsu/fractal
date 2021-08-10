"""

    *What Is Possible?*

"""


"""
    available_actions(::AbstractGameEnv)

Return the vector of all available actions.
"""
function available_actions(game::AbstractGameEnv)
  mask = actions_mask(game)
  return actions(spec(game))[mask]
end


"""

    *Possible Is What.*

"""

class Possible(Is, What,):
    pass
