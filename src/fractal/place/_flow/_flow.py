# function GI.vectorize_state(::RL.AbstractEnv, state)
#   @assert isa(state, Array{<:Number}) "
#   Your state is not a vector and so you should define `vectorize_state`"
#   return convert(Array{Float32}, state)
# end

# default_vectorize_state(rl, state) = GI.vectorize_state(rl, state)

# GI.symmetries(::RL.AbstractEnv, state) = Tuple{typeof(state), Vector{Int}}[]

# default_symmetries(rl, state) = GI.symmetries(rl, state)

# default_heurisic_value(rl)   = GI.heuristic_value(rl)
# default_render(rl)           = GI.render(rl)
# default_action_string(rl, a) = GI.action_string(rl, a)
# default_parse_action(rl, s)  = GI.parse_action(rl, s)
# default_read_state(rl)       = GI.read_state(rl)
