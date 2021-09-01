from dataclasses import dataclass


@dataclass
class Reflection:
    glimpse: Glimpse
    multiprocessing: Multiprocessing
    update_threshold: float
