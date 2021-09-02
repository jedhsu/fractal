//! Realizing describes The state of the world at the present time.

pub struct Realizing(
    World,
):
    @abstractmethod
    fn read_state(&self):
        \\\!
        Read a state from stdin.
        \\\!
        pass

    @abstractmethod
    fn pri32_state(&self):
        \\\!
        Write a state to stdout.
        \\\!
        pass
