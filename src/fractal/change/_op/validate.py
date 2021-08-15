"""

    *Validate*

  validate parameters.

"""

class Validate(Parameters,):
    pass


def check_params(gspec: AbstractGameSpec, p: Params,):
    errors = String[]
    warns = String[]

    # Collecting all relevant params
    mctss = [p.self_play.mcts]
    sims = [p.self_play.sim]

    if !isnothing(p.arena):
        push!(mctss, p.arena.mcts)
        push!(sims, p.arena.sim)

    if any(sim.batch_size > sim.num_workers for sim in sims):
        push!(errors,
          "The number of simulation workers must be " *
          "greater or equal than the inference batch size.")
        end

    # Detecing non-provided symmetries
    if any(sim.flip_probability != 0 for sim in sims):
        state = GI.current_state(GI.init(gspec))
        if isempty(GI.symmetries(gspec, state)):
          push!(errors, "You must specify some game symmetries to use flip_probability>0.")
        return (errors, warns)
