from .._brain import Brain

pub trait Plasticity {
    fn parameters(&self);
    //! Return the collection of trainable parameters of a brain.
    
    fn regularized_parameters(&self);
    //! Return the collection of regularized parameters of a network.
    //! This usually excludes neuron's biases.
    
    fn number_of_parameters(&self);
    //! Return the total number of parameters of a network.

    fn number_of_regularized_parameters(&self);
    //! Return the total number of regularized parameters of a network.

impl Plasticity for Brain {
    fn parameters(&self) {}

    fn regularized_parameters(&self) {}

    fn number_of_parameters(&self) {
        return sum(len(p) for p in &self.parameters())
    }

    fn number_of_regularized_parameters(&self) {
        return sum(len(p) for p in &self.regularized_parameters())
    }
}
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
