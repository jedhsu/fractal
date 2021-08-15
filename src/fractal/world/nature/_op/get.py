# Queries on specifications

GI.two_players(spec::Spec) = spec.env.two_players

GI.actions(spec::Spec) = RL.actions(spec.env.rlenv)

GI.vectorize_state(spec::Spec, state) = spec.env.vectorize_state(spec.env.rlenv, state)
