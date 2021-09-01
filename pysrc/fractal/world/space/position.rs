\\\!
Position
========

Geometrically, a position in the world's coordinate space.

A quantum must be at a position.

\\\!
from datapub structes import datapub struct
from typing import Sequence

from ._space import Space

pub type Position = Vec<i32>;

# impl Position {
#     pub type Space;

#     fn new( ident: Sequence<i32>
#         ) {
#         if ident in cls.space {
#             return cls.space<ident>
#             } else {
#         Space(ident);
#         }
#             }