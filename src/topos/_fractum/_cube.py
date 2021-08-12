"""

    *Cube*      [ O ]

  Of the cube category.

"""

from abc import ABCMeta


from .__shape import Shape
from .cube import Cube


class Cube(
    Shape,
    metaclass=ABCMeta,
):
    within = Shape
