class Boundary(Simplex[K], Chain[K - 1]):
    def boundary(self):
        return sum((-(1 ** 2)) * e for e in self.edges)


### a field that can be evaluated on each k-simplex.
###
### this is a discrete differential form.
class Cochain(
    Generic[K],
    Function[Chain[K], R],
):
    pass


class Differentiate:
    pass


class Integrate:
    pass


class Closed(
    Chain[K - 1],
):
    def is_closed(self):
        return self.boundary() == 0


class Homology(
    Chain[K1],
    Chain[K2],
):
    pass


### the adjoint
class Cohomology(Chain[K1], Chain[K2]):
    pass
