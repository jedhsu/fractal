"""

    *Globe*     [ I ]

  Of the globe category.

"""

from abc import ABCMeta


from .__shape import Shape


class Globe(
    Shape,
    metaclass=ABCMeta,
):
    left = Shape
    right = Shape

    def __class_getitem__(cls):
        pass
