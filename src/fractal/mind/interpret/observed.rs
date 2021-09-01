//! Statistics for games with ternary rewards

pub struct Glimpsed {
    n_won: i16,
    n_draw: i16,
    n_lost: i16,
}

impl Glimpsed {
    fn from_passion(rewards::AbstractVector{<:Number}) {
        num_won  = count(==(1), rewards);
        num_draw = count(==(0), rewards);
        num_lost = count(==(-1), rewards);
        // @assert num_won + num_draw + num_lost == length(rewards)
        TernaryOutcomeStatistics {n_won, n_draw, n_lost }
    }

    fn from_evaluated(evaluated: &Evaluated) {
        TernaryOutcomeStatistics { report.rewards }
    }
}
