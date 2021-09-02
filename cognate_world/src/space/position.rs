//! Geometrically, a position in the world's coordinate space.
//!
//! A quantum must be at a position.


pub type Position = Vec<i32>;

impl Position {
    pub type Space;

    fn new(ident: Vec<i32>) {
        if ident in cls.space {
            return cls.space<ident>
        } else {
            Space(ident);
        }
    }
}
