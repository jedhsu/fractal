//! Evaluate the value of the searched futures.

pub trait Interpret {
    fn interpret(&self, glimpsing: Glimpsing, action: Action, energy: Energy) {};
}

impl Interpret for Glimpsing {
    fn interpret(
        &self,
        realized: WorldState,
        action: Action,
        energy: Energy,
    ):
        stats = worldstate.tree<state>.stats
        astats = stats<action_id>
        stats<action_id> = PlacementAnalysis(
            astats.P,
            astats.W + q,
            astats.N + 1,
        )
}
