"""

    *Am I*

  The Big Bang.

"""


class Am(
    I,
):
    def am_i(
        self,
        this,
    ):
        this = init(self)
        return cls(this)


class I(
    Am,
):
    pass


#     init(::AbstractGameSpec, state) :: AbstractGameEnv

# Create a new game environment, initialized in a given state.
# """
