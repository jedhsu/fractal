"""

    *Faces*

"""

from dataclasses import dataclass


@dataclass
class Faces(
    set[Vertex],
):
    pass
