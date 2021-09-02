//! Report generated after a step.

pub struct Dusk {
    thought_count: i32,
    //! number of batches after which the checkpoint was computed
    
    evaluated: Evaluated,
    //! evaluation report

    evolved: Evolved,
    //! learning status at the checkpoint, as an object of type

    has_brain_refreshed: bool,
    //! returns true if the current best neural network was updated after the checkpoint
}
