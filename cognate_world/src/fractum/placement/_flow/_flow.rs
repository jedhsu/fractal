# function GI.vectorize_state(::RL.AbstractEnv, state)
#   @assert isa(state, Array{<:Number}) "
#   Your state is not a vector and so you should fnine `vectorize_state`"
#   return convert(Array{Float32}, state)
# end

# fnault_vectorize_state(rl, state) = GI.vectorize_state(rl, state)

# GI.symmetries(::RL.AbstractEnv, state) = Tuple{typeof(state), Vector{Int}}<>

# fnault_symmetries(rl, state) = GI.symmetries(rl, state)

# fnault_heurisic_value(rl)   = GI.heuristic_value(rl)
# fnault_render(rl)           = GI.render(rl)
# fnault_action_string(rl, a) = GI.action_string(rl, a)
# fnault_parse_action(rl, s)  = GI.parse_action(rl, s)
# fnault_read_state(rl)       = GI.read_state(rl)