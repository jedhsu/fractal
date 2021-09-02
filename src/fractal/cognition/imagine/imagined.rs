//! Statistics for games with ternary rewards

pub struct Imagined {
    number_of_wins: i16,
    number_of_draws: i16,
    number_of_losses: i16,
}

impl Imagined {
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
