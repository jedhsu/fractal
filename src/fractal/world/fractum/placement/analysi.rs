pub struct Analysis {
    state: State,
    some_boolean: bool,
}

impl Analysis:
    fn initialize(
        spacetime: Spacetime,
        placing: Place,
    ):
        if placing in spacetime.tree {
            return (env.tree<state>, false);
        } else {
            let (P, V) = env.oracle(state);
            let info = init_state_info(P, V, env.prior_temperature);
            let env.tree<state> = info;
            Analysis {info: info, some_boolean: true}
        }
}
