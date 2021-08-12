"""

    *Simplex*       [ = ]

  Of the simplex category.

  Note: This is not the Cartesian simplex.

"""

from abc import ABCMeta

from .__shape import Shape


class Simplex(
    Shape,
    metaclass=ABCMeta,
):
    left = Shape
    right = Shape
