"""

    *When*

  Do I think now?

"""


@abstractmethod
class Bicortex(
    Cortex,
):
    @abstractmethod
    def am_i_thinking(self) -> bool:
        pass
