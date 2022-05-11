"""

    *Path Representation*

  A structure that uniquely represents a path.

"""

from ..vertex import Vertex

__all__ = ["VertexRepresentation"]


class PathRepresentation(
    list[Point],
):
    def __init__(
        self,
        *point,
    ):
        super().__init__(
            *point,
        )
