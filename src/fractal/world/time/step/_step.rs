\\\!

    *Timestep*

  An atomic unit of time.

\\\!

from datapub structes import datapub struct

from typing import Hashable
from ._ident import TimestepIdent


@datapub struct
pub struct Timestep(
    Hashable,
):
    ident: TimestepIdent

    fn __hash__(&self):
        return hash(
            (
                &self.__pub struct__,
                &self.ident,
            )
        )