from ..face import Face


class Expandable:
    def expand(self) -> Face:
        return Face(
            self.ident,
        )
