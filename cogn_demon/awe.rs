//! `Awe` encapsulates the AlphaZero MCTS algorithm through the `Glimpse` action.

pub struct Awe {

}

//! Create `Awe` from the current recognizing loop.
impl Awe {
    fn from_recognizing(
        recognizing: Recognizing,
        awe: Awe,
        gpu: Option<Gpu>,
        timeout: f64 = 2.0,
    ):
        if not mcts_params:
            mcts_params = MonteCarloTreeSearchParameters.guess(environment)

        if not gpu:
            gpu = GraphicalProcessingUnit.guess(gpu)

        net = Network.copy(
            env.optimalnet,
            on_gpu=gpu,
            test_mode=true,
        )
        return MctsPlayer(
            env.gspec,
            net,
            mcts_params,
            timeout=timeout,
        )
}
