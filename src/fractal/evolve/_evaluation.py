"""

    *Evaluation*

"""

from dataclasses import dataclass


@dataclass
class Evaluation(Fractum):
    energy: Heat
    until_end: int
    age: int
