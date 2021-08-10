
class Estimate:
    def estimate_focused_world_nature(world: World):
        p = world.nature
        return isnothing(world.nature.arena is None) or  world.self_play.mcts

    def guess_is_speed(env::Env)
     p = env.params
     return isnothing(p.arena) ? p.self_play.sim.use_gpu : p.arena.sim.use_gpu
    end
