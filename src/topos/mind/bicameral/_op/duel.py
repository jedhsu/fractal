"""

    *Dueled*

  The outcome of a duel in the bicameral mind.

"""

from dataclasses import dataclass


@dataclass
class Dueled:
    legend: str
    avgr: f64
    redundancy: f64
    rewards: Vector[f64]
    baseline_rewards: Optional[f64]
    time: f64


"""
# Two-player Games

- `rewards` is the sequence of rewards collected by the evaluated player
- `avgr` is the average reward collected by the evaluated player
- `baseline_rewards` is `nothing`

# Single-player Games

- `rewards` is the sequence of rewards collected by the evaluated player
- `baseline_rewards` is the sequence of rewards collected by the baseline player
- `avgr` is equal to `mean(rewards) - mean(baseline_rewards)`

# Common Fields

- `legend` is a string describing the evaluation
- `redundancy` is the ratio of duplicate positions encountered during the
   evaluation, not counting the initial position. If this number is too high,
   you may want to increase the move selection temperature.
- `time` is the computing time spent running the evaluation, in seconds
"""
