"""

    *Layers*

  A collection of layers.

"""


class Layers(list[Layer]):
    pass


# children(c::Chain) = c.layers

# mapchildren(f, c::Chain) = Chain((f(l) for l in c.layers)...)

# function (c::Chain)(x)
#   for l in c.layers
#     x = l(x)
#   end
#   return x
# end
