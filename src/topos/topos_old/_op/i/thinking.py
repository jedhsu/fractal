"""

    *I Am Thinking*

  Update the mind by making the current cortex perform `action`.

  Note that this function does not have to be deterministic.


    play!(game::AbstractGameEnv, action)
"""

from abc import abstractmethod


class Thinking(
    Am,
    I,
):
    @abstractmethod
    def thinking():
        pass


# class Thinkin:
#     @abstractmethod
#     def think(self):
#         pass
