#####
##### Utilities for distributed game simulation
#####

# This code factorizes out all the complexity of:
#   1. Batching inference requests across game simulations
#   2. Distributing simulations across multiple machines (optional)
"""
    record_trace

A measurement function to be passed to a [`Simulator`](@ref) that produces
named tuples with two fields: `trace::Trace` and `colors_flipped::Bool`.
"""
record_trace(t, cf, p) = (trace=t, colors_flipped=cf)


# From a vector of measures, extract all rewards w.r.t. white and compute redundancy
# `samples` is a vector of named tuples with fields `trace` and `colors_flipped`
function rewards_and_redundancy(samples; gamma)
  rewards = map(samples) do s
    wr = total_reward(s.trace, gamma)
    return s.colors_flipped ? -wr : wr
  end
  states = [st for s in samples for st in s.trace.states]
  redundancy = compute_redundancy(states)
  return rewards, redundancy
end



"""

REPORTS

"""

class Evolved:
    loss: Loss
    Hp:  Float32 # property of the memory, constant during a learning iteration
    Hpnet:  Float32

class Observed:
    num_samples:  Int
    num_boards:  Int
    Wtot:  Float32
    status:  LearningStatus

class StageSamples:
    min_remaining_length:  Int
    max_remaining_length:  Int
    samples_stats:  Samples
end

class Perfs:
    time:  Float64
    allocated:  Int64
    gc_time:  Float64
end

class Epoched:
    perfs_self_play:  Perfs
    perfs_memory_analysis:  Perfs
    perfs_learning:  Perfs

    self_play:  SelfPlay
    memory:  Union{Memory, Nothing}
    learning:  Learning
end

class Initial:
    num_network_parameters:  Int
    num_network_regularized_parameters:  Int
    mcts_footprint_per_node:  Int
    errors: Vector[str]
    warnings: Vector[str]

class Memory:
    latest_batch:  Samples
    all_samples:  Samples
    per_game_stage:  Vector{StageSamples}

const Benchmark = Vector{Evaluation}


"""

PLAY

"""
#####
##### Interface for players
#####

#####
##### Player with a custom temperature
#####

"""
    PlayerWithTemperature{Player} <: AbstractPlayer

A wrapper on a player that enables overwriting the temperature schedule.
"""
struct PlayerWithTemperature{P} <: AbstractPlayer
  player :: P
  temperature :: AbstractSchedule{Float64}
end

function think(p::PlayerWithTemperature, game)
  return think(p.player, game)
end

function reset!(p::PlayerWithTemperature)
  reset!(p.player)
end

function player_temperature(p::PlayerWithTemperature, game, turn)
  return p.temperature[turn]
end

# Alternative constructor
function MctsPlayer(
    game_spec::AbstractGameSpec, oracle, params::MctsParams; timeout=nothing)
  mcts = MCTS.Env(game_spec, oracle,
    gamma=params.gamma,
    cpuct=params.cpuct,
    noise_ϵ=params.dirichlet_noise_ϵ,
    noise_α=params.dirichlet_noise_α,
    prior_temperature=params.prior_temperature)
  return MctsPlayer(mcts,
    niters=params.num_iters_per_turn,
    τ=params.temperature,
    timeout=timeout)
end

# MCTS with random oracle
function RandomMctsPlayer(game_spec::AbstractGameSpec, params::MctsParams)
  oracle = MCTS.RandomOracle()
  mcts = MCTS.Env(game_spec, oracle,
    cpuct=params.cpuct,
    gamma=params.gamma,
    noise_ϵ=params.dirichlet_noise_ϵ,
    noise_α=params.dirichlet_noise_α)
  return MctsPlayer(mcts,
    niters=params.num_iters_per_turn,
    τ=params.temperature)
end

function think(p::MctsPlayer, game)
  if isnothing(p.timeout) # Fixed number of MCTS simulations
    MCTS.explore!(p.mcts, game, p.niters)
  else # Run simulations until timeout
    start = time()
    while time() - start < p.timeout
      MCTS.explore!(p.mcts, game, p.niters)
    end
  end
  return MCTS.policy(p.mcts, game)
end

function player_temperature(p::MctsPlayer, game, turn)
  return p.τ[turn]
end

function reset_player!(player::MctsPlayer)
  MCTS.reset!(player.mcts)
end

#####
##### Network player
#####

function player_temperature(p::TwoPlayers, game, turn)
  if GI.white_playing(game)
    return player_temperature(p.white, game, turn)
  else
    return player_temperature(p.black, game, turn)
  end
end

######
###### Simple utilities to play an interactive game
######

#"""
#    Human <: AbstractPlayer

#Human player that queries the standard input for actions.

#Does not implement [`think`](@ref) but instead implements
#[`select_move`](@ref) directly.
#"""
#struct Human <: AbstractPlayer end

#struct Quit <: Exception end

#function select_move(::Human, game, turn)
#  a = nothing
#  while isnothing(a) || a ∉ GI.available_actions(game)
#    print("> ")
#    str = readline()
#    print("\n")
#    isempty(str) && throw(Quit())
#    a = GI.parse_action(GI.spec(game), str)
#  end
#  return a
#end

#"""
#    interactive!(game)
#    interactive!(gspec)
#    interactive!(game, player)
#    interactive!(gspec, player)
#    interactive!(game, white, black)
#    interactive!(gspec, white, black)

#Launch a possibly interactive game session.

#This function takes either an `AbstractGameSpec` or `AbstractGameEnv` as an argument.
#"""
#function interactive! end

#function interactive!(game::AbstractGameEnv, player)
#  try
#  GI.render(game)
#  turn = 0
#  while !GI.game_terminated(game)
#    action = select_move(player, game, turn)
#    GI.play!(game, action)
#    GI.render(game)
#    turn += 1
#  end
#  catch e
#    isa(e, Quit) || rethrow(e)
#    return
#  end
#end

#interactive!(gspec::AbstractGameSpec, player) = interactive!(GI.init(gspec), player)

#interactive!(game, white, black) = interactive!(game, TwoPlayers(white, black))

#interactive!(game) = interactive!(game, Human(), Human())
"""
EVAL UTIL
"""


"""
Utilities to evaluate players against one another.

Typically, between each training iteration, different players
that possibly depend on the current neural network
compete against a set of baselines.
"""
module Benchmark

using ..AlphaZero

using ProgressMeter
using Statistics: mean
using Base: @kwdef

"""
    Benchmark.Player

Abstract type to specify a player that can be featured in a benchmark duel.

Subtypes must implement the following functions:
  - `Benchmark.instantiate(player, nn)`: instantiate the player specification
      into an [`AbstractPlayer`](@ref) given a neural network
  - `Benchmark.name(player)`: return a `String` describing the player
"""
abstract type Player end

# instantiate(::Player, gspec, nn)
function instantiate end

# name(::Player) :: String
function name end


"""
    Duel <: Evaluation

Evaluating a player by pitting it against a baseline player in a two-player game.
"""
@kwdef struct Duel <: Evaluation
  player :: Player
  baseline :: Player
  sim :: SimParams
end

name(s::Single) = name(s.player)

name(d::Duel) = "$(name(d.player)) / $(name(d.baseline))"

"""
    Benchmark.run(env::Env, duel::Benchmark.Evaluation, progress=nothing)

Run a benchmark duel and return a [`Report.Evaluation`](@ref).

If a `progress` is provided, `next!(progress)` is called
after each simulated game.
"""
function run end

function run(env::Env, eval::Evaluation, progress=nothing)
  net() = Network.copy(env.bestnn, on_gpu=eval.sim.use_gpu, test_mode=true)
  if isa(eval, Single)
    simulator = Simulator(net, record_trace) do net
      instantiate(eval.player, env.gspec, net)
    end
  else
    @assert isa(eval, Duel)
    simulator = Simulator(net, record_trace) do net
      player = instantiate(eval.player, env.gspec, net)
      baseline = instantiate(eval.baseline, env.gspec, net)
      return TwoPlayers(player, baseline)
    end
  end
  samples, elapsed = @timed simulate(
    simulator, env.gspec, eval.sim,
    game_simulated=(() -> next!(progress)))
  gamma = env.params.self_play.mcts.gamma
  rewards, redundancy = rewards_and_redundancy(samples, gamma=gamma)
  return Report.Evaluation(
    name(eval), mean(rewards), redundancy, rewards, nothing, elapsed)
end
#####
##### Standard players
#####

"""
    Benchmark.MctsRollouts(params) <: Benchmark.Player

Pure MCTS baseline that uses rollouts to evaluate new positions.

Argument `params` has type [`MctsParams`](@ref).
"""
struct MctsRollouts <: Player
  params :: MctsParams
end

name(p::MctsRollouts) = "MCTS ($(p.params.num_iters_per_turn) rollouts)"

function instantiate(p::MctsRollouts, gspec::AbstractGameSpec, nn)
  return MctsPlayer(gspec, MCTS.RolloutOracle(gspec), p.params)
end

"""
    Benchmark.Full(params) <: Benchmark.Player

Full AlphaZero player that combines MCTS with the learnt network.

Argument `params` has type [`MctsParams`](@ref).
"""
struct Full <: Player
  params :: MctsParams
end

name(::Full) = "AlphaZero"

function instantiate(p::Full, gspec::AbstractGameSpec, nn)
  return MctsPlayer(gspec, nn, p.params)
end

"""
    Benchmark.NetworkOnly(;τ=1.0) <: Benchmark.Player

Player that uses the policy output by the learnt network directly,
instead of relying on MCTS.
"""
@kwdef struct NetworkOnly <: Player
  τ :: Float64 = 1.0
end

name(::NetworkOnly) = "Network Only"

function instantiate(p::NetworkOnly, ::AbstractGameSpec, nn)
  player = NetworkPlayer(nn)
  return PlayerWithTemperature(player, ConstSchedule(p.τ))
end

"""
    Benchmark.MinMaxTS(;depth, τ=0.) <: Benchmark.Player

Minmax baseline, which relies on [`MinMax.Player`](@ref).
"""
@kwdef struct MinMaxTS <: Player
  depth :: Int
  amplify_rewards :: Bool
  τ :: Float64 = 0.
end

name(p::MinMaxTS) = "MinMax (depth $(p.depth))"

function instantiate(p::MinMaxTS, ::AbstractGameSpec, nn)
  return MinMax.Player(
    depth=p.depth, amplify_rewards=p.amplify_rewards, τ=p.τ)
end

end

"""




SPACETIME 


"""

"""
A generic interface for single-player games and two-player zero-sum games.

Stochastic games and intermediate rewards are supported. By convention,
rewards are expressed from the point of view of the player called _white_.
In two-player zero-sum games, we call `black` the player trying to minimize the reward.
"""
module GameInterface

export AbstractGameSpec, AbstractGameEnv

using ..AlphaZero: Util

#####
##### Game environments and game specifications
#####

# NAMING CONVENTION:
# - A game specification is usually written: `game_spec` or `gspec`.
# - A game environment is usually written: `game` or `g`.
#   We usually avoid `env` as it is too generic and can clash with the name for an
#   MCTS environment or training environment.
# - A state is usually written: `state` or `s`.
# - An action is usually written: `action` or `a`.

#####
##### Queries on specs
#####

"""
    two_players(::AbstractGameSpec) :: Bool

Return whether or not a game is a two-players game.
"""
function two_players end

"""
    actions(::AbstractGameSpec)

Return the vector of all game actions.
"""
function actions end

#####
##### Operations on envs
#####
"""
    actions_mask(::AbstractGameEnv)

Return a boolean mask indicating what actions are available.

The following identities must hold:

  - `game_terminated(game) || any(actions_mask(game))`
  - `length(actions_mask(game)) == length(actions(spec(game)))`
"""
function actions_mask end





"""
    heuristic_value(game::AbstractGameEnv)

Return a heuristic estimate of the state value for the current player.

The given state must be nonfinal and returned values must belong to the
``(-∞, ∞)`` interval.

This function is not needed by AlphaZero but it is useful for building
baselines such as minmax players.
"""
function heuristic_value end



