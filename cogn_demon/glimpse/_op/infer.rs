
fn infer_glimpse_parameters(world: Realizing) {
    let prm = world.parameters;
    if (prm.glimpse is None) {prm.reflection.mcts} else {prm.arena.glimpse}  // TODO fuck dont ge tit
}

fn infer_gpu_use(world: Realizing) {
// #  p = env.params
// #  return isnothing(p.arena) ? p.&self_play.sim.use_gpu : p.arena.sim.use_gpu
// # end
}
