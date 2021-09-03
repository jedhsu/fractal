//! Report generated after a step.

pub struct Dusk<Checkpoint> {
    recognized: Recognized,
    //! Report describing the cognition status.
    
    evolved: Evolved,
    //! Report describing the evolution status.

    thought_count: i32,
    //! Number of batches after which the checkpoint was computed


    has_brain_refreshed: bool,
    //! Asks whether the current best neural network was updated after the checkpoint.
}
