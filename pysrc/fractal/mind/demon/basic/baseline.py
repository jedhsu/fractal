# """
#     Benchmark.MinMaxTS(;depth, τ=0.) <: Benchmark.Player

# Minmax baseline, which relies on [`MinMax.Player`](@ref).
# """
# @kwdef struct MinMaxTS <: Player
#   depth :: Int
#   amplify_rewards :: Bool
#   τ :: Float64 = 0.
# end

# name(p::MinMaxTS) = "MinMax (depth $(p.depth))"

# def instantiate(p::MinMaxTS, ::AbstractGameSpec, nn)
#   return MinMax.Player(
#     depth=p.depth, amplify_rewards=p.amplify_rewards, τ=p.τ)
