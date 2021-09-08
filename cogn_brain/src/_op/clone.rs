pub trait Clone {
    fn clone(&self, shall_use_gpu: bool, is_testing: bool);
}

impl Clone for Brain {
    fn clone(
        &self,
        shall_use_gpu: bool,
        is_testing: bool,
    ) -> Brain {
        let network = &self.clone();

        if network.on_gpu() {
            network.move_to_gpu();
        } else if {
            network.move_to_cpu();
        }

        network
    }
}
