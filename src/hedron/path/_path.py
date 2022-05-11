"""

    *Path*

"""


from .vertex import Vertex


@dataclass
class Path(
    PathRepresetation,
):
    def __init__(
        self,
        *point: Vertex,
    ):
        super().__init__(
            [*point],
        )
