
pub trait Awaken {
    fn awaken(&self) -> Awakened;
}

impl Awaken for Cognition {
    fn awakened(&self):
        return Awakened(
            &self.current_brain.number_parameters(),
            &self.smartest_brain.number_regularized_parameters(),
            Demon(
                &self.nature,
                &self.current_brain,
                &self.parameters.&self_play.mcts,
            ),
        )
}
