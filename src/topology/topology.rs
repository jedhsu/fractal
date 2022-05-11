use num::traits::Unsigned as Nat

/// The topological n-simplex.
///
/// Defined using the Kan complex perspective,
/// which is most useful for us.
pub trait N_Δ_: C<N, S> {
    /// Homeomorphic to the Cartesian N-ball.
    pub fn homeomorphism();
    


}
        Ball<N>
    }

/// The Infinity Groupoid.
///
/// Contains all morphisms.
pub trait Infinity_Groupoid {
}

/// Homotopic map. Weaker than homeomorphism.
pub trait Deform<Y: Topology> {
    fn deform(&self) {
    }
}

// Ray tracing generalized to topologies.
pub trait HomeomorphicProjection<S, T>
where
    S: Topology,
    T: Embedded<Topology>,
{
    fn homeomorphism(&self);
}

pub trait Ray<D, P>
where
    D: Direction,
    P: Point,
{
    // pub direction: D;
    // pub point: P,
}

// pub trait View<C, R> where C, R: Unsigned;
