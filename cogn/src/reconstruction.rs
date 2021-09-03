//! The static data to reconstruct a session.

pub struct Reconstruction {
    name: &str,

    rules: Rules,
    //! Parameters describing the environment world.
  
    cognition: Cognition,
    //! Parameters controlling the process of cognition.

    make_nn: Fn,
    //! `mknet` is a neural network constructor taking arguments `(netparams, gspec)`

    neuroplasticity: Neuroplasticity
    //! Parameters describing the neural network architecture.

    // benchmark :: Vector{<:Benchmark.Evaluation}
}
