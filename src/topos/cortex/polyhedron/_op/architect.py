"""

    *Construct*

  Construct the polyhedron architecture.

"""


class Construct(
    Polyhedron,
):
    def Polyhedron(
        size,
        n,
        bnmom,
    ):
        pad = size / 2
        layers = Chain(
            Conv(
                size,
                pad=pad,
            ),
            BatchNorm(
                n,
                relu,
                momentum=bnmom,
            ),
            Conv(
                size,
                pad=pad,
            ),
            BatchNorm(
                n,
                momentum=bnmom,
            ),
        )
        # return Chain(
        # SkipConnection(layers, +),
        # (lambda x: relu.x),)
