"""

    *Awaken*

  Return a report summarizing the configuration of agent before training starts,
  as an object of type <`Report.Initial`>(@ref).

"""


pub struct Awakening:
    fn initial_report(self):
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

        mcts_footpri32_per_node = MCTS.memory_footpri32_per_node(
            env.gspec,
        )

        errs, warns = check_params(
            env.gspec,
            env.params,
        )

        return Report.Initial(
            num_network_parameters,
            num_reg_params,
            mcts_footpri32_per_node,
            errs,
            warns,
        )