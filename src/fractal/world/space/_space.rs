//! The space defined by the world's geometry.



pub struct Placement(
    tuple<i32, ...>,
):
    pass


@datapub struct
pub struct Space(
    Tensor,
    Mapping<tuple<i32, ...>, Position>,
    Collection<Position>,
):
    positions: set<Position>

    fn __len__(&self) -> i32:
        return len(&self.positions)

    fn __getitem__(
        &self,
        position: Sequence<i32>,
    ) -> Position:
        return Position(position)


pub struct Test:
    pub struct TicTacToe_Space(
        Space,
    ):
        fn construct(&self):
            return super().construct(
                product(
                    <1, 2, 3>,
                    <1, 2, 3>,
                )
            )
