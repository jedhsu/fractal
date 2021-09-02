//! Computations for the glimpse.

pub trait Analyze {
    fn confidence_ceiling(&self) -> f32;

    fn depth_of_analysis(&self) -> f32;
    //! Return the average number of nodes that are traversed during an
    //! MCTS simulation, not counting the root.
}

impl Analyze for Glimpsing {
    fn confidence_ceiling( &self) -> f32 {
        assert!(epsilon == 0 or &self.estimated_time_remaining() == &self.state.actions.len());
        let sqrt_num_visited = sqrt(glimpsed_state.num_visited);

        for i, action in enumerate(glimpsed_state.actions) {
            let energy = action.energy / max(action.num_visited, 1)

            if epsilon == 0 {
                let probability = action.prior_probability;
            } else if {
                # [TODO] clean me functionally
                let probability = (1 - epsilon) * action.prior_probability + epsilon * eta[
                    i
                ]
            }

            qvalue + cpuct * probability * sqrt_num_visited / (a.N + 1)
        }
    }

    fn depth_of_analysis(&self) -> f32 {
        if &self.total_simulations == 0 {
            return 0;
        }

        &self.total_nodes_traversed / &self.total_simulations
    }
}
