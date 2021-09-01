//! Report generated after a step.

pub struct Dusk {
    /// number of batches after which the checkpoint was computed
    batch_id: i32,
    /// evaluation report
    evaluated: Evaluated,
    /// learning status at the checkpoint, as an object of type
    evolved: Evolved,
    /// true if the current best neural network was updated after the checkpoint
    has_brain_refreshed: bool,
}
