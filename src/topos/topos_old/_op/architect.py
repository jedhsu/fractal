"""

    *[Architect] Lattice Topology*

"""

class Architect(LatticeTopology,):
    def architect(gestalt: Gestalt, evolution: Evolution,)
        bnmom = hyper.batch_norm_momentum
        function make_dense(indim, outdim)
        if hyper.use_batch_norm
          Chain(
            Dense(indim, outdim),
            BatchNorm(outdim, relu, momentum=bnmom))
        else
          Dense(indim, outdim, relu)
        end
        # indim = prod(GI.state_dim(gspec))
        # outdim = GI.num_actions(gspec)
        # hsize = hyper.width
        # hlayers(depth) = [make_dense(hsize, hsize) for i in 1:depth]
        # common = Chain(
        # flatten,
        # make_dense(indim, hsize),
        # hlayers(hyper.depth_common)...)
        # vhead = Chain(
        # hlayers(hyper.depth_vhead)...,
        # Dense(hsize, 1, tanh))
        # phead = Chain(
        # hlayers(hyper.depth_phead)...,
        # Dense(hsize, outdim),
        # softmax)
        return Lattice(gspec, hyper, common, vhead, phead,)
