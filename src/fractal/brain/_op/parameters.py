from .._brain import Brain


class Parameters(
    Brain,
):
    def parameters(self):
        """
        Return the collection of trainable parameters of a network.
        """
        raise NotImplementedError

    def regularized_parameters(self):
        """
        Return the collection of regularized parameters of a network.
        This usually excludes neuron's biases.
        """
        raise NotImplementedError

    def number_of_parameters(self):
        """
            num_parameters(::AbstractNetwork)

        Return the total number of parameters of a network.
        """
        return sum(len(p) for p in self.parameters())

    def number_of_regularized_parameters(self):
        """
        Return the total number of regularized parameters of a network.
        """
        return sum(len(p) for p in self.regularized_parameters())
