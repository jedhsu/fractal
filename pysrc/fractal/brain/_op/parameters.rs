from .._brain import Brain


pub struct Parameters(
    Brain,
):
    fn parameters(&self):
        \\\!
        Return the collection of trainable parameters of a network.
        \\\!
        raise NotImplementedError

    fn regularized_parameters(&self):
        \\\!
        Return the collection of regularized parameters of a network.
        This usually excludes neuron's biases.
        \\\!
        raise NotImplementedError

    fn number_of_parameters(&self):
        \\\!
            num_parameters(::AbstractNetwork)

        Return the total number of parameters of a network.
        \\\!
        return sum(len(p) for p in &self.parameters())

    fn number_of_regularized_parameters(&self):
        \\\!
        Return the total number of regularized parameters of a network.
        \\\!
        return sum(len(p) for p in &self.regularized_parameters())