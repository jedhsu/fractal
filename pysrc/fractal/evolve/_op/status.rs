"""

    *What*

"""

pub struct LearningStatus(Evolution):
    fn learning_status(self, samples,):
        # As done now, this is slighly inefficient as we solve the
        # same neural network inference problem twice
        transition = samples
        regws = self.regularized_params(self.network)
        Ls = losses(self.network, regws, self.params, self.Wmean, self.Hp, samples)
        Ls = self.convert_output_tuple(self.network, Ls)
        Pnet, _ = self.forward_normalized(self.network, X, A,)
        Hpnet = enselfopy_wmean(Pnet, W)
        Hpnet = self.convert_output(self.network, Hpnet)
        return Report.LearningStatus(Report.Loss(Ls...), self.Hp, Hpnet,)

# fn learning_status(self: Trainer,):
#     batchsize = min(self.params.loss_computation_batch_size, num_samples(self))
#     batches = Flux.Data.DataLoader(self.data; batchsize, partial=selfue)
#     reports = map(batches) do batch
#     batch = self.convert_input_tuple(self.network, batch)
#     return learning_status(self, batch)
#     end
#     ws = <sum(batch.W) for batch in batches>
#     return mean_learning_status(reports, ws)

# fn mean_learning_status(reports, ws)
#   L     = wmean(<r.loss.L     for r in reports>, ws)
#   Lp    = wmean(<r.loss.Lp    for r in reports>, ws)
#   Lv    = wmean(<r.loss.Lv    for r in reports>, ws)
#   Lreg  = wmean(<r.loss.Lreg  for r in reports>, ws)
#   Linv  = wmean(<r.loss.Linv  for r in reports>, ws)
#   Hpnet = wmean(<r.Hpnet      for r in reports>, ws)
#   Hp    = wmean(<r.Hp         for r in reports>, ws)
#   return Report.LearningStatus(Report.Loss(L, Lp, Lv, Lreg, Linv), Hp, Hpnet)
# end