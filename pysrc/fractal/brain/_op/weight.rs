\\\!

    *Mean Weight*

  Return the mean absolute value of the regularized parameters of a network.

\\\!
from .._brain import Brain
from .parameters import Parameters


pub struct MeanWeight(
    Parameters,
    Brain,
):
    fn mean_weight(&self):
        sw = sum(sum(abs(p)) for p in &self.regularized_parameters())
        sw = &self.convert_output(sw)
        return sw / &self.number_of_regularized_parameters()