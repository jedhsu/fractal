
"""
    simulate_distributed(::Simulator, ::AbstractGameSpec, ::SimParams; <kwargs>)

Identical to [`simulate`](@ref) but splits the work across all available distributed
workers, whose number is given by `Distributed.nworkers()`.
"""

class Vision:
    def glimpse(
        self,
        spacetime: Spacetime,
        game_simulated
    ):
        spawn()
        distribute()
        validate()

    def spawn(self): 
        # Spawning a task to keep count of completed simulations
        chan = Distributed.RemoteChannel(()->Channel{Nothing}(1))
        Util.@tspawn_mainfor i in 1:p.num_games
            take!(chan)
            game_simulated()
        glimpsed = put!(chan, nothing)

    def distribute():
        num_each, rem = divrem(p.num_games, Distributed.nworkers())
        assert num_each >= 1
        workers = Distributed.workers()
        tasks = map(workers) do w
        Distributed.@spawnat w begin
            Util.@printing_errors begin
                simulate(
                simulator,
                gspec,
                SimParams(p; num_games=(w == workers[1] ? num_each + rem : num_each)),
                game_simulated=remote_game_simulated)
            results = fetch.(tasks)
    
    def validate():
        # If one of the worker raised an exception, we print it
        for r in results:
            if isinstance(r, Distributed.RemoteException):
                showerror(stderr, r, catch_backtrace())
        return reduce(vcat, results)

# function compute_redundancy(states)
#   unique = Set(states)
#   return 1. - length(unique) / length(states)
# end
