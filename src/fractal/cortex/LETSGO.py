


"""
    game_spec(::AbstractNetwork)

Return the game specification that was passed to the network's constructor.
"""
function game_spec end

to_singletons(x) = reshape(x, size(x)..., 1)
from_singletons(x) = reshape(x, size(x)[1:end-1])


#####
##### Derived functions
#####



"""
    gc(::AbstractNetwork)

Perform full garbage collection and empty the GPU memory pool.
"""
function gc end
