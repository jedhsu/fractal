
pub trait Light {
    /// The speed of light.
    ///
    /// It is "dimensionless" but it is really not, dimensions are not built fo constructive case
    /// like this.
    ///
    /// Dimensions are all other els in vector field / self in vector field.
    ///
    /// The dimensions are blinks of not self / blink.
    const _c_ = 299_729_458;
}


pub struct Path<N> {
    initial_timestep: u64,
    n_oscillations: u64,
    last_point: &u64,
}

impl<N> Path {
    fn speed(&self, current_timestep: u64) -> f64 {
        self.initial_timestep / n_oscillations;
    }
}

pub trait Condition {
    faces_left: mut set<Simplex<dim-1>>;
}

pub trait ReferenceFrame {
    fn relative_to(&self, other: Self) -> fn
}

/// The frame of reference of a path defined under a certain distance / Hilbert space.
///
/// Start with no biasing on the vertices part, change later?
pub trait Path {
    fn factor(&self);
}

/// Color is a 2D Simplex, and we perceive it as a discrete space.

/// The electromagnetic wave can propagate through space.

/// WOW the it has to be considered one isomorphic struct idea is actually legit.
///
pub trait Pathing {
}

pub struct Network {
    vertices: u64 = 1000000,
    edges_per_vertex: u64 = 1000,
}

pub trait Topos {

}

/// The possible space of events that can be causally influenced.
///
/// Analagous to the light-cone of general relativity.
///
/// In general relativity, you are bounded by vision. Here you are bounded by oscillation.
///
/// It is like music, but the energy is higher.
///

pub struct LightField {
    paths: Path<
}

/// These are homotopy levels.
pub struct PathLevel<N> {
    level: N,
    paths: Vec<Simplex<N>>
}

/// This could be 2 dimensions higher.
pub struct Oscillation<N> {

}

pub struct Present {

}

pub trait Optimize {
}
