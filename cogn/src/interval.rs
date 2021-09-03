pub enum Period {
    //! Describes units of time relevant to the process of cognition.
    //!
    //! These are universal, so are relevant for:
    //!
    //!   + a single training iteration
    //!   + a single training experiment
    //!
    
    Day,
    //! A single training iteration.
    
    Year,
    //! A single entire training experiment is defined to take a year.
}

// TODO these should be parametrized!
pub enum IntradayPeriod {
    Morning,
    Afternoon,
    Evening,
    //! 
}
