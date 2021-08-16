
#####
##### Training handlers
#####

"""
    Handlers

Namespace for the callback functions that are used during training.
This enables logging, saving and plotting to be implemented separately.
An example handler object is `Session`.

All callback functions take a handler object `h` as their first argument
and sometimes a second argment `r` that consists in a report.

| `training_finished(h)`      | called once at the end of training             |
"""
class Events:
  import ..Report

  def iteration_started(h)      return end
    AtBigBang

  def self_play_started(h)      return end
    AtReflecting
  def game_played(h)            return end
    AtGlimpsedReflection
  def self_play_finished(h, r)  return end
    AtReflected
  def memory_analyzed(h, r)     return end
    AtAnalyzing
  def learning_started(h)       return end
    AtEvolving

  def updates_started(h)        return end
    AtRewiring
  def updates_finished(h, r)    return end
    AtRewired

    AtDawn(
  def checkpoint_started(h)     return end
    AtDueling
  def checkpoint_game_played(h) return end
    AtDusk
  def checkpoint_finished(h, r) return end
    AtDueled
  def learning_finished(h, r)   return end
    AtEvolved
  def iteration_finished(h, r)  return end
    AtBigCrunch
  def training_finished(h)      return end

end

"""
| Callback                    | Comment                                        |
|:----------------------------|:-----------------------------------------------|
| `iteration_started(h)`      | called at the beggining of an iteration        |
| `self_play_started(h)`      | called once per iter before self play starts   |
| `game_played(h)`            | called after each game of self play            |
| `self_play_finished(h, r)`  | sends report: [`Report.SelfPlay`](@ref)        |
| `memory_analyzed(h, r)`     | sends report: [`Report.Memory`](@ref)          |
| `learning_started(h)`       | called at the beginning of the learning phase  |
| `updates_started(h, r)`     | sends report: [`Report.LearningStatus`](@ref)  |
| `updates_finished(h, r)`    | sends report: [`Report.LearningStatus`](@ref)  |
| `checkpoint_started(h)`     | called before a checkpoint evaluation starts   |
| `checkpoint_game_played(h)` | called after each arena game                   |
| `checkpoint_finished(h, r)` | sends report: [`Report.Checkpoint`](@ref)      |
| `learning_finished(h, r)`   | sends report: [`Report.Learning`](@ref)        |
| `iteration_finished(h, r)`  | sends report: [`Report.Iteration`](@ref)       |
"""
