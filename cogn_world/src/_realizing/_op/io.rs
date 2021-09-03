//! Realizing describes The state of the world at the present time.

pub struct Realizing(
    World,
):
    @abstractmethod
    unsafe fn from_stdin(&self):
        //! Read a state from stdin.

    @abstractmethod
    unsafe fn into_stdout(&self) {
        //!  Write a state to stdout.
    }
