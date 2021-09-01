from typing import Union


pub struct Gpu:
    fn convert_output(self):
        """
            convert_output(::AbstractNetwork, output)

        Convert an array (or number) produced by a neural network
        to a standard CPU array (or number) type.
        """
        pass

    fn convert_output_tuple(self, output: Union<tuple, NamedTuple>):
        pass
        # return map(output) do arr

    # convert_output(nn, arr)