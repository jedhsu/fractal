"""

    *Evaluation*

"""


@dataclass
class Evaluation(Fractum):
    energy: Heat
    until_end: int
    age: int