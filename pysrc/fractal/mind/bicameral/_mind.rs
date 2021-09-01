\\\!

    *Bicameral Mind*

\\\!

from datapub structes import datapub struct

from .._mind import Mind
from ..unicameral import UnicameralMind


@datapub struct
pub struct BicameralMind(
    Mind,
):
    white: UnicameralMind
    black: UnicameralMind