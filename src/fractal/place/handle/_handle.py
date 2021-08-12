
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
| `training_finished(h)`      | called once at the end of training             |
"""
module Handlers

  import ..Report

  function iteration_started(h)      return end
  function self_play_started(h)      return end
  function game_played(h)            return end
  function self_play_finished(h, r)  return end
  function memory_analyzed(h, r)     return end
  function learning_started(h)       return end
  function updates_started(h)        return end
  function updates_finished(h, r)    return end
  function checkpoint_started(h)     return end
  function checkpoint_game_played(h) return end
  function checkpoint_finished(h, r) return end
  function learning_finished(h, r)   return end
  function iteration_finished(h, r)  return end
  function training_finished(h)      return end

end
