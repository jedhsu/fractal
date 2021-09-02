//! Benchmark.MinMaxTS(;depth, τ=0.) <: Benchmark.Player
// # Minmax baseline, which relies on <`MinMax.Player`>(@ref).
// # \\\!

pub struct Minimax {
    depth: i32,
    amplify_rewards: bool,
    tau: f64,
}

impl Display {
    // # name(p::MinMaxTS) = "MinMax (depth $(p.depth))"
}


fn new(minimax: Minimax, nature: Nature, brain: Brain) {
    MinMax.Player { depth: minimax.depth, amplify_rewards: minimax.amplify_rewards, tau: minimax.τ }
}
