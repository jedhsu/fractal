pub trait Symmetry: AbstractSymmetry {
    fn rotate(&self, x: i32, y: i32) -> (i32, i32);
    fn vflip(&self, x: i32, y: i32) -> (i32, i32);
    fn ap(&self, eval: Fn) -> Fn;
    fn sym(&self, eval: Fn) -> Fn;
    // fn dihedral_symmetries(&self, eval: Fn) -> Fn;
}

//! can be a lot cleaner...
impl Symmetry for TicTacToe {
    const N = &Self.BOARD_SIDE;

    fn rotate(
        x: i32,
        y: i32,
    ) -> (i32, i32) {
        (y, N - x + 1)
    }

    fn vflip(
        x: i32,
        y: i32,
    ) -> (i32, i32) {
        ( x, cls.N - y + 1,)
    }

    fn ap(&self, eval: Fn) -> Fn {
        pos_of_xy(fn(xy_of_pos(pos)))
    }

    fn sym(&self, eval: Fn) -> Fn { }

    // fn dihedral_symmetries():
    //     pass
}
