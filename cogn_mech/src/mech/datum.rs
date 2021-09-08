//! A datum specifies a type of element found in the World that can occupy a number of states.

pub struct Datum<I: Ident, S: State> {
    ident: I,
    //! The identifier of the datum.
    
    state: S,
    //! The state of the vector., where states is enum.
}

pub trait Datum {
    type S;
    
    fn ident(&self) -> Ident;
    //! Returns the unique name of a datum.
    
    fn state(&self) -> State;
    //! Returns the state of a datum.
    
    fn from_statespace(statespace: S) -> State;
    //! Initializes from state space.
}


#[cfg(test)]
pub mod tests {
    impl DatumTest for 

    #[test]
    fn Datum
}

//pub struct Calculate:
//    fn vectorize_place(&self, state):
//        pass

////! vectorize_state(::AbstractGameSpec, state) :: Array{Float32}

//Return a vectorized representation of a given state.
//\\\!
//function vectorize_state end
