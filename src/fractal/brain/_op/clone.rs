//! A clone function that also handles CPU/GPU transfers.

pub trait Clone {
    fn clone(&self, on_gpu: bool, is_testing: bool);
}

impl Clone for Brain {
    fn clone(
        &self,
        on_gpu: bool,
        test_mode: bool,
    ):
        network = &self.clone()
        if network.on_gpu() {
            network.move_to_gpu()
        } else {
            network.move_to_cpu()
        }
        return network
}
