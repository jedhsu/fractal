//! Metrics on the configuration of agent before training starts,
//! as an object of type <`Report.Initial`>(@ref).


pub struct Awakened {
    number_parameters: i32
    number_regularized_parameters: i32
    demon: Demon
    memory_footpri32_per_node: i32
}

fn awaken(&self) -> Awakened:
    num_network_parameters = Network.num_parameters(
        env.curnn,
    )

    num_reg_params = Network.num_regularized_parameters(
        env.curnn,
    )

    player = MctsPlayer(
        env.gspec,
        env.curnn,
        env.params.&self_play.mcts,
    )

    mcts_footpri32_per_node = MCTS.memory_footpri32_per_node(
        env.gspec,
    )

    errs, warns = check_params(
        env.gspec,
        env.params,
    )

    Awakened(
        num_network_parameters,
        num_reg_params,
        mcts_footpri32_per_node,
        errs,
        warns,
    )
}
