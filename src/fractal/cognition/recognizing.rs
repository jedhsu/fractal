//! The stateful environment of cognition.
//!
//! The environment features
//!   - the current neural network
//!   - the best neural network seen so far that is used for data generation
//!   - a memory buffer
//!   - an iteration counter

pub struct Recognizing {
    cognition: Cognition,
    //! The cognition parameters.

    nature: Nature,
    //! The laws of the global environment.

    conscious: Brain,
    //! The current neural network.

    wisdom: Brain,
    //! The best-performing neural network thus far.

    memory: Memory,
    //! The memory buffer.

    age: Age,
    //! THe iteration count.
}

fn cognite(nature: Nature, mind: Mind, conscious: Brain, wisdom: Brain, experience, age: Age) {
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

