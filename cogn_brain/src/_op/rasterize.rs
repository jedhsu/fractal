from typing import Union


pub trait Rasterize {
    fn convert_output(&self, output);
    fn convert_output_tuple(&self, output);
}

impl Rasterize for Brain {
    fn convert_output(&self, output) {
        //! Convert an array (or number) produced by a neural network
        //! to a standard CPU array (or number) type.
        
        
    }

    fn convert_output_tuple(&self, output: Union<tuple, NamedTuple>):
        pass
        # return map(output) do arr

    fn convert_output(nn, arr)
}
