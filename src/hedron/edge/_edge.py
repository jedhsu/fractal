"""

    *Edge*

  An edge.

  This is a presheaf.

"""

from dataclasses import dataclass

from ..vertex import Vertex


@dataclass
class Edge:
    left: Vertex
    right: Vertex
