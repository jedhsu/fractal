//! Environment of the mind.
//!
//! The environment features the current neural network, the best neural network
//! seen so far that is used for data generation, a memory buffer
//! and an iteration counter.

pub struct Cognition {
    /// Specifies the laws of the environment world.
    nature: Nature,

    /// `params` has type [`Params`](@ref)
    params: Parameters,

    /// The current neural network and has type [`AbstractNetwork`](@ref)
    conscious: Brain,

    /// The best neural network so far, which is used for data generation
    wisdom: Brain,

    /// `experience` is the initial content of the memory buffer
    /// as a vector of [`TrainingSample`](@ref)
    processing: Processing,

    /// `age` is the value of the iteration counter (0 at the start of training)
    age: Age,
}

impl Cognition {
    fn new(nature: Nature, mind: Mind, conscious: Brain, wisdom: Brain, experience, age: Age) {
        let msize = max(params.mem_buffer_size[itc], length(experience));
        let memory = MemoryBuffer(gspec, msize, experience);
        // return new{typeof(gspec), typeof(curnn), GI.state_type(gspec)}(
// #   gspec, params, curnn, bestnn, memory, itc)
// # end
    }

// \\\!
// # Constructor

//     Env(game_spec, params, curnn, bestnn=copy(curnn), experience=[], itc=0)

// Construct a new AlphaZero environment:
// \\\!

