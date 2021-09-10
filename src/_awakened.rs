//! Metrics on the configuration of agent before training starts,
//! as an object of type <`Report.Initial`>(@ref).

pub struct Awakened {
    number_of_parameters: i32,

    number_of_regularized_parameters: i32,

    demon: Demon,

    memory_footprint_per_node: i32,
}
