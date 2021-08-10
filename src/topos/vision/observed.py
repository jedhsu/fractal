

#####
##### Statistics for games with ternary rewards
#####

@dataclass
class TernaryOutcomeStatistics:
  num_won: Int
  num_draw: Int
  num_lost: Int

function TernaryOutcomeStatistics(rewards::AbstractVector{<:Number})
  num_won  = count(==(1), rewards)
  num_draw = count(==(0), rewards)
  num_lost = count(==(-1), rewards)
  @assert num_won + num_draw + num_lost == length(rewards)
  return TernaryOutcomeStatistics(num_won, num_draw, num_lost)
end

function TernaryOutcomeStatistics(report::Report.Evaluation)
  return TernaryOutcomeStatistics(report.rewards)
end

