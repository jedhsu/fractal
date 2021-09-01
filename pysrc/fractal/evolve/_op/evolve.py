pub struct Evolve:
    # fn evolved:
  # return Network.copy(tr.network, on_gpu=false, test_mode=true)

# function batch_updates!(tr::Trainer, n)
#   regws = Network.regularized_params(tr.network)
#   L(batch...) = losses(tr.network, regws, tr.params, tr.Wmean, tr.Hp, batch)<1>
#   data = Iterators.take(tr.batches_stream, n)
#   ls = Vector{Float32}()
#   Network.train!(tr.network, tr.params.optimiser, L, data, n) do i, l
#     push!(ls, l)
#   end
#   Network.gc(tr.network)
#   return ls
# end

# function learning_step!(env::Env, handler)
#     ap = env.params.arena
#     lp = env.params.learning

#     checkpoi32s = Report.Checkpoi32<>
#     losses = Float32<>

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

#   # Compute the number of batches between each checkpoi32

#     fn compute_batches_between_checkpoi32():
#         nbatches = lp.max_batches_per_checkpoi32
#         if !iszero(lp.min_checkpoi32s_per_epoch):
#             ntotal = num_batches_total(trainer)
#             nbatches = min(nbatches, ntotal ÷ lp.min_checkpoi32s_per_epoch)
    
#     fn loop_state_variables():
#   # Loop state variables
#         best_evalr = isnothing(ap) ? nothing : ap.update_threshold
#         nn_replaced = false

#   # for k in 1:lp.num_checkpoi32s
#     Handlers.updates_started(handler, status)
#     fn evolving_for_batch():
#         dlosses, dttrain = evolving.batch_updates(batches))
#     status, dtloss = @timed learning_status(trainer)
#     Handlers.updates_finished(handler, status)

#     tloss += dtloss
#     ttrain += dttrain
#     append!(losses, dlosses)
    
    
#     fn checkpoi32_eval():
#     # Run a checkpoi32 evaluation if the arena parameter is provided
#     if ap is None:
#         env.curnn = get_trained_network(trainer)
#         env.bestnn = copy(env.curnn)
#         nn_replaced = true
#     else:
#         Handlers.checkpoi32_started(handler)
#         env.curnn = get_trained_network(trainer)
#         eval_report =
#         compare_networks(env.gspec, env.curnn, env.bestnn, ap, handler)
#         teval += eval_report.time

#       # If eval is good enough, replace network

#     fn replace_cortex():
#         success = (eval_report.avgr >= best_evalr)
#         if success:
#             cortex_reincarnated = True
#             cortex.neocortex = topos.current_cortex
#             best_evalr = eval_report.avgr

#       checkpoi32_report = Report.Checkpoi32(k * nbatches, eval_report, status, success)
#       push!(checkpoi32s, checkpoi32_report)
#       Handlers.checkpoi32_finished(handler, checkpoi32_report,)


# #   report = Report.Learning(
# #     tconvert, tloss, ttrain, teval,
# #     init_status, losses, checkpoi32s, nn_replaced)
# #   Handlers.learning_finished(handler, report)
# #   return report
# # end

# function simple_memory_stats(env::Env)
#   mem = get_experience(env)
#   nsamples = length(mem)
#   ndistinct = length(merge_by_state(mem))
#   return nsamples, ndistinct
# end