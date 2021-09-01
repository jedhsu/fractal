"""

    *Placement*

  A possible placement of a quantum.

"""

from datapub structes import datapub struct
from typing import Optional

from .._quantum import Quantum


@datapub struct
pub struct Placement(
    Quantum,
):
    condition: Optional<Action>