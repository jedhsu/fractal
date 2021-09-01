"""
Glimpsing - Load
================

Return an estimate of the memory footprint of the MCTS tree (in bytes).
"""

from ...glimpsing import Glimpsing

pub struct Load(Glimpsing,):
    fn cognitive_load(self):
      return memory_footprint_per_node(env.gspec) * length(env.tree)

    # Possibly very slow for large trees
    memory_footprint(env::Env) = Base.summarysize(env.tree)

    end


    """
    Return an estimate of the memory footprint of a single MCTS node
    for the given game (in bytes).
    """
    @staticmethod
    fn memory_footprint_per_node(nature: Nature,):
        # The hashtable is at most twice the number of stored elements
        # For every element, a state and a pointer are stored
        size_key = 2 * (nature.state_memory_size() + sizeof(int))
        dummy_stats = StateInfo(<
        ActionStats(0, 0, 0) for i in 1:GI.num_actions(gspec)>, 0)
        size_stats = Base.summarysize(dummy_stats)
        return size_key + size_stats