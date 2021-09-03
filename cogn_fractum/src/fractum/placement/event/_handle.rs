//! Handles
//!
//! Namespace for the callback functions that are used during training.
//! This enables logging, saving and plotting to be implemented separately.
//!
//! An example handler object is `Session`.
//!
//! All callback functions take a handler object `h` as their first argument
//! and sometimes a second argment `r` that consists in a report.

// | `training_finished(h)`      | called once at the end of training             |


mod event  {
  import ..Report

  fn episode_started(h)      return end
  //! Sends Birth.

  fn &self_play_started(h)      return end
    AtReflecting
  //! sends Start of Odyssey.

  fn game_played(h)            return end
  //! Sends Reflected.

  fn &self_play_finished(h, r)  return end
  //! Sends Return from Odyssey.

  fn memory_analyzed(h, r)     return end
  //! Sends Analyzed.

  fn learning_started(h)       return end
  //! Sends Evolving.

  fn updates_started(h)        return end
  //! Sends Calibrating..

  fn updates_finished(h, r)    return end
  //! Sends Calibrated..

  fn checkpoi32_started(h)     return end
  //! Sends Start of War..

  fn checkpoi32_game_played(h) return end
  //! Sends Dueled.

  fn checkpoi32_finished(h, r) return end
  //! Sends End of War.

  fn learning_finished(h, r)   return end
  //! Sends Evolved.

  fn iteration_finished(h, r)  return end
  //! Sends Death.

  fn training_finished(h)      return end

end
