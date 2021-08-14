"""

    *Interpreted*

   Metrics generated after interpreted a vision.

"""

from dataclasses import dataclass


@dataclass
class Interpreted:
    num_won: int
    num_draw: int
    num_lost: int


# function TernaryOutcomeStatistics(rewards::AbstractVector{<:Number})
#   num_won  = count(==(1), rewards)
#   num_draw = count(==(0), rewards)
#   num_lost = count(==(-1), rewards)
#   @assert num_won + num_draw + num_lost == length(rewards)
#   return TernaryOutcomeStatistics(num_won, num_draw, num_lost)
# end

# function TernaryOutcomeStatistics(report::Report.Evaluation)
#   return TernaryOutcomeStatistics(report.rewards)
# end
