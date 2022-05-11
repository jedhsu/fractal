"""

    *Vertex*

"""

from dataclasses import dataclass

from .edge import Edge

__all__ = ["Vertex"]


@dataclass
class Vertex(
    VertexRepresentation,
    Expand,
):
    ident: str
    edges: set[Edge]
