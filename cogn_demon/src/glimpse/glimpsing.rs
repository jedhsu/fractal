//! The environment state of a `Glimpse`.


pub struct Glimpsing(
    Glimpse,
):
    parameters: Glimpse,
    //! Glimpse parameters.

    nature: Nature,
    //! The parameters describing the world's rules.

    interpreter: Demon,
    //! External oracle to evaluate positions

    vision: HashMap<State, Analysis>,
    //! Store (nonterminal) state statistics assuming the white player is to play
    
    number_of_paths: u64,
    //! The number of glimpsed paths.
    
    unique_visits: u64,
    //! The number of unique states visited.

}

