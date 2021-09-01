\\\!
Measure
=======

\\\!

from .._thinking import Thinking


pub struct Measure(
    Thinking,
):
    fn __len__(&self):
        return len(&self.thermodynamics)

    fn total_energy(&self):
        pass