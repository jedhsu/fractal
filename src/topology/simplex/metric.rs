pub trait MetricTopology<S> {
    fn metric(
        left: &S,
        right: &S,
    ) -> f64;
}

// impl MetricTopology for Topology {

// }
