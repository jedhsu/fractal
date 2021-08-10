class Evolve:
    # def evolved:
  # return Network.copy(tr.network, on_gpu=false, test_mode=true)

# function batch_updates!(tr::Trainer, n)
#   regws = Network.regularized_params(tr.network)
#   L(batch...) = losses(tr.network, regws, tr.params, tr.Wmean, tr.Hp, batch)[1]
#   data = Iterators.take(tr.batches_stream, n)
#   ls = Vector{Float32}()
#   Network.train!(tr.network, tr.params.optimiser, L, data, n) do i, l
#     push!(ls, l)
#   end
#   Network.gc(tr.network)
#   return ls
# end

def learning_status(tr: Trainer, samples,):
    W, X, A, P, V = samples
    regws = Network.regularized_params(tr.network)
    Ls = losses(tr.network, regws, tr.params, tr.Wmean, tr.Hp, samples,)
    Ls = Network.convert_output_tuple(tr.network, Ls)
    Pnet, _ = Network.forward_normalized(tr.network, X, A)
    Hpnet = entropy_wmean(Pnet, W)
    Hpnet = Network.convert_output(tr.network, Hpnet)
    return Report.LearningStatus(Report.Loss(Ls), tr.Hp, Hpnet)

# function learning_step!(env::Env, handler)
#     ap = env.params.arena
#     lp = env.params.learning

#     checkpoints = Report.Checkpoint[]
#     losses = Float32[]

#     tlossteval, ttrain = 0., 0., 0.
#     experience = get_experience(env.memory)
#     if env.params.use_symmetries:
#         experience = augment_with_symmetries(env.gspec, experience)
#     if isempty(experience):
#     # Skipping the learning phase
#         return dummy_learning_report()

#     trainer, tconvert = Trainer(env.gspec, env.curnn, experience, lp,)

#     init_status = learning_status(trainer)
#     status = init_status
#     Handlers.learning_started(handler)

#   # Compute the number of batches between each checkpoint

#     def compute_batches_between_checkpoint():
#         nbatches = lp.max_batches_per_checkpoint
#         if !iszero(lp.min_checkpoints_per_epoch):
#             ntotal = num_batches_total(trainer)
#             nbatches = min(nbatches, ntotal ÷ lp.min_checkpoints_per_epoch)
    
#     def loop_state_variables():
#   # Loop state variables
#         best_evalr = isnothing(ap) ? nothing : ap.update_threshold
#         nn_replaced = false

#   # for k in 1:lp.num_checkpoints
#     Handlers.updates_started(handler, status)
#     def evolving_for_batch():
#         dlosses, dttrain = evolving.batch_updates(batches))
#     status, dtloss = @timed learning_status(trainer)
#     Handlers.updates_finished(handler, status)

#     tloss += dtloss
#     ttrain += dttrain
#     append!(losses, dlosses)
    
    
#     def checkpoint_eval():
#     # Run a checkpoint evaluation if the arena parameter is provided
#     if ap is None:
#         env.curnn = get_trained_network(trainer)
#         env.bestnn = copy(env.curnn)
#         nn_replaced = true
#     else:
#         Handlers.checkpoint_started(handler)
#         env.curnn = get_trained_network(trainer)
#         eval_report =
#         compare_networks(env.gspec, env.curnn, env.bestnn, ap, handler)
#         teval += eval_report.time

#       # If eval is good enough, replace network

#     def replace_cortex():
#         success = (eval_report.avgr >= best_evalr)
#         if success:
#             cortex_reincarnated = True
#             cortex.neocortex = topos.current_cortex
#             best_evalr = eval_report.avgr

#       checkpoint_report = Report.Checkpoint(k * nbatches, eval_report, status, success)
#       push!(checkpoints, checkpoint_report)
#       Handlers.checkpoint_finished(handler, checkpoint_report,)


# #   report = Report.Learning(
# #     tconvert, tloss, ttrain, teval,
# #     init_status, losses, checkpoints, nn_replaced)
# #   Handlers.learning_finished(handler, report)
# #   return report
# # end

# function simple_memory_stats(env::Env)
#   mem = get_experience(env)
#   nsamples = length(mem)
#   ndistinct = length(merge_by_state(mem))
#   return nsamples, ndistinct
# end
