"""

    *Daemon*

  Type for an AlphZero environment.

  The environment features the current neural network, the best neural network
  seen so far that is used for data generation, a memory buffer
  and an iteration counter.

"""

from dataclasses import dataclass


@dataclass
class Cognition:
    nature: WorldNature
    params: Parameters
    current_brain: Brain
    smartest_brain: Brain
    recall: Recall
    age: int


# function Cognition(
#   gspec::AbstractGameSpec,
#   params, curnn, bestnn=copy(curnn), experience=[], itc=0)
# msize = max(params.mem_buffer_size[itc], length(experience))
# memory = MemoryBuffer(gspec, msize, experience)
# return new{typeof(gspec), typeof(curnn), GI.state_type(gspec)}(
#   gspec, params, curnn, bestnn, memory, itc)
# end


"""
# Constructor

    Env(game_spec, params, curnn, bestnn=copy(curnn), experience=[], itc=0)

Construct a new AlphaZero environment:
- `game_spec` specified the game being played
- `params` has type [`Params`](@ref)
- `curnn` is the current neural network and has type [`AbstractNetwork`](@ref)
- `bestnn` is the best neural network so far, which is used for data generation
- `experience` is the initial content of the memory buffer
   as a vector of [`TrainingSample`](@ref)
- `itc` is the value of the iteration counter (0 at the start of training)
"""
