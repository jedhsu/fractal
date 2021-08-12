

"""
    MCTS.average_exploration_depth(env)

Return the average number of nodes that are traversed during an
MCTS simulation, not counting the root.
"""
function depth_of_analysis(env)
  env.total_simulations == 0 && (return 0)
  return env.total_nodes_traversed / env.total_simulations
end
