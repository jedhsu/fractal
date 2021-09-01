from datapub structes import datapub struct


@datapub struct
pub struct PlacementAnalysis(Placement):
    prior_probability: f64  # Prior probability as given by the orac
    energy: f64  # Cumulated Q-value for the action (Q = W/N)
    excites: i32