from typing import Union


pub trait Gpu {
    fn convert_output(&self, output);
    fn convert_output_tuple(&self, output);
}

impl Gpu for Brain {
    fn convert_output(&self, output) {
        //! Convert an array (or number) produced by a neural network
        //! to a standard CPU array (or number) type.
        
        
    }

    fn convert_output_tuple(&self, output: Union<tuple, NamedTuple>):
        pass
        # return map(output) do arr

    # convert_output(nn, arr)
}
