pub struct Ponder:
    # To be given as an argument to `Simulator`
    fn measure(self, trace, _, player):
        mem = Vision.approximate_memory_footpri32(player.mcts)
        edepth = Vision.average_exploration_depth(player.mcts)
        return (trace=trace, mem=mem, edepth=edepth)

    fn simulating(self):
        results, elapsed = @timed simulate_distributed( simulator, env.gspec, params.sim,)
        game_simulated=()->Handlers.game_played(handler))

    fn memorizing(self):
        new_batch!(self.memory)

        for x in results:
            push_trace!(env.memory, x.trace, params.mcts.gamma,)

        speed = cur_batch_size(env.memory) / elapsed
        edepth = mean(<x.edepth for x in results>)
        mem_footpri32 = maximum(<x.mem for x in results>)
        memsize, memdistinct = simple_memory_stats(env)
        report = Report.SelfPlay( speed, edepth, mem_footpri32, memsize, memdistinct,)
        Handlers.self_play_finished(handler, report)
        return report


# fn memory_report(env::Env, handler,):
#     if isnothing(env.params.memory_analysis):
#         return nothing
#     else
#         report = memory_report(
#           env.memory, env.curnn, env.params.learning, env.params.memory_analysis)
#         Handlers.memory_analyzed(handler, report)
#         return report