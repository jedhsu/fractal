

#####
##### GameInterface API
#####

GI.clone(env::Env) = @set env.rlenv = RL.clone(env.rlenv)

GI.set_state!(env::Env, state) = RL.setstate!(env.rlenv, state)

GI.spec(env::Env) = Spec(env)


# Operations on environments

GI.current_state(env::Env) = RL.state(env.rlenv)

GI.game_terminated(env::Env) = RL.terminated(env.rlenv)

GI.white_playing(env::Env) = RL.player(env.rlenv) == 1

GI.actions_mask(env::Env) = RL.valid_action_mask(env.rlenv)

GI.white_reward(env::Env) = env.last_reward

GI.heuristic_value(env::Env) = env.heuristic_value(env.rlenv)

# Symmetries

GI.symmetries(spec::Spec, state) = spec.env.symmetries(spec.env.rlenv, state)

# Interactive utilities

GI.render(env::Env) = env.render(env.rlenv)


end

