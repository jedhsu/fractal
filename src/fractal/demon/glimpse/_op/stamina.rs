//! Return an estimate of the memory footpri32 of the MCTS tree (in bytes).

pub trait Stamina {
    fn weight(&self, nature: Nature) -> i32;
    //! Return an estimate of the memory footpri32 of a single MCTS node
    //! for the given game (in bytes).

    fn pressure(&self, nature: Nature) -> f64;
    //! The hashtable is at most twice the number of stored elements
    //! For every element, a state and a poi32er are stored
}

impl  Stamina for Glimpsing {
}

//     fn pressure(&self):
//       return memory_footpri32_per_node(env.gspec) * length(env.tree)

//     # Possibly very slow for large trees
//     memory_footpri32(env::Env) = Base.summarysize(env.tree)

//     end


//     \\\!
//     \\\!
//     @staticmethod
//     fn memory_footpri32_per_node(nature: Nature,):
//         size_key = 2 * (nature.state_memory_size() + sizeof(i32))
//         dummy_stats = StateInfo(<
//         ActionStats(0, 0, 0) for i in 1:GI.num_actions(gspec)>, 0)
//         size_stats = Base.summarysize(dummy_stats)
//         return size_key + size_stats
