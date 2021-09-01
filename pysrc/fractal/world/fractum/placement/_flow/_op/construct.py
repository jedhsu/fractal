pub struct 

fn .init(spec::Spec):
  env = GI.clone(spec.env)
  RL.reset!(env.rlenv)
  return env
end

function GI.init(spec::Spec, state)
  env = GI.clone(spec.env)
  RL.setstate!(env.rlenv, state)
  return env
end