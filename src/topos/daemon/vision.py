"""

    *Daemon Vision*

"""

class Dueled(Daemon, Vision,):
    num_won: Int
    num_draw: Int
    num_lost: Int

class TernaryOutcom
function TernaryOutcomeStatistics(rewards::AbstractVector{<:Number})
    count_won  = count(==(1), rewards)
    count_draw = count(==(0), rewards)
    count_lost = count(==(-1), rewards)
    assert sum(num_won + num_draw + num_lost,) == length(rewards)
    return TernaryOutcomeStatistics(num_won, num_draw, num_lost)

function TernaryOutcomeStatistics(report::Report.Evaluation)
  return TernaryOutcomeStatistics(report.rewards)
end
