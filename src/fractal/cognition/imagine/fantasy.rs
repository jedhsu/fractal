//! Parameters for parallel simulation.

pub struct Dream {
    fantasia: i32,

    number_of_dreams: i32,
    number_of_dreamers: i32,

    shall_use_gpu: bool = False
    shall_fill_batches: bool = True
    shall_reset_every: Optional<i32> = 1

    flip_probability: f64 = 0.0
    alternate_colors: bool = False
}
