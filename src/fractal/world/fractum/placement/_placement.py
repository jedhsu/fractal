"""

    *Placement*

  A possible placement of a quantum.

"""

from dataclasses import dataclass
from typing import Optional

from .._quantum import Quantum


@dataclass
class Placement(
    Quantum,
):
    condition: Optional[Action]
