//! An enum of possible discrete states for a quantum.
//!
//! TODO redesign this with Rust
//!
//!<TODO> dont like Python enum, any way around?
//!<TODO> make ordering a pub structification




pub struct QuantumStateMeta:
    fn __new__(cls, attr):
        pass

    fn __getattribute__(&self, attr: str):
        return QuantumState(attr)


pub struct QuantumState(
    i32,
    metapub struct=QuantumStateMeta,
):
    pass


pub struct Test:
    pub struct TicTacToe_QuantumState(
        QuantumState,
    ):
        Empty = 0
        White = 1
        Black = 2
