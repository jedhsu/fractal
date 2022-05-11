"""

    *Face*

  Talk about the isomorphism
  between edges and points.

"""

from dataclasses import dataclass

__all__ = ["Face"]


class FaceRepresentations(
    Ring[AdjacentEdges],
):
    pass


class Collapse:
    def collapse(self) -> Vertex[Shrink]:
        """
        Collapses the face into a point.
        """


@dataclass
class Face(
    Collapse,
    Reduce,
    FaceRepresentations,
):
    pass
