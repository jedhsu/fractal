"""
Abstract Statics
================

"""

from abc import ABCMeta
from abc import abstractmethod


class AbstractStatics(
    metaclass=ABCMeta,
):
    @abstractmethod
    def initial_time(cls) -> WorldTime:
        pass

    @abstractmethod
    def initial_position(cls) -> WorldPosition:
        pass

    @classmethod
    def initial_worldstate(cls) -> WorldState:
        raise NotImplementedError

    @abstractmethod
    @classmethod
    def has_world_ended(cls) -> bool:
        raise NotImplementedError
