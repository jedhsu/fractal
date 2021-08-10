class Ponder:
    # To be given as an argument to `Simulator`
    def measure(self, trace, _, player):
        mem = Vision.approximate_memory_footprint(player.mcts)
        edepth = Vision.average_exploration_depth(player.mcts)
        return (trace=trace, mem=mem, edepth=edepth)

    def simulating(self):
        results, elapsed = @timed simulate_distributed( simulator, env.gspec, params.sim,)
        game_simulated=()->Handlers.game_played(handler))

    def memorizing(self):
        new_batch!(self.memory)

        for x in results:
            push_trace!(env.memory, x.trace, params.mcts.gamma,)

        speed = cur_batch_size(env.memory) / elapsed
        edepth = mean([x.edepth for x in results])
        mem_footprint = maximum([x.mem for x in results])
        memsize, memdistinct = simple_memory_stats(env)
        report = Report.SelfPlay( speed, edepth, mem_footprint, memsize, memdistinct,)
        Handlers.self_play_finished(handler, report)
        return report


# def memory_report(env::Env, handler,):
#     if isnothing(env.params.memory_analysis):
#         return nothing
#     else
#         report = memory_report(
#           env.memory, env.curnn, env.params.learning, env.params.memory_analysis)
#         Handlers.memory_analyzed(handler, report)
#         return report
