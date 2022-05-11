@dataclass
class Edges(
    set[Edge],
):
    def __init__(
        self,
        *edge: Edge,
    ):
        super(Edges, self).__new__(
            set,
            *edge,
        )
