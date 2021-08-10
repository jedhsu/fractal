"""

    *Awaken*

  Return a report summarizing the configuration of agent before training starts,
  as an object of type [`Report.Initial`](@ref).

"""


class Awaken:
    def initial_report(self):
        num_network_parameters = Network.num_parameters(
            env.curnn,
        )

        num_reg_params = Network.num_regularized_parameters(
            env.curnn,
        )

        player = MctsPlayer(
            env.gspec,
            env.curnn,
            env.params.self_play.mcts,
        )

        mcts_footprint_per_node = MCTS.memory_footprint_per_node(
            env.gspec,
        )

        errs, warns = check_params(
            env.gspec,
            env.params,
        )

        return Report.Initial(
            num_network_parameters,
            num_reg_params,
            mcts_footprint_per_node,
            errs,
            warns,
        )
