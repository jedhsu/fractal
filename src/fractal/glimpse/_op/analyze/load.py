

"""
    MCTS.approximate_memory_footprint(env)

Return an estimate of the memory footprint of the MCTS tree (in bytes).
"""
function cognitive_load(env::Env)
  return memory_footprint_per_node(env.gspec) * length(env.tree)
end

# Possibly very slow for large trees
memory_footprint(env::Env) = Base.summarysize(env.tree)

end

