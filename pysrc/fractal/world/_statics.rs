"""
Abstract Statics
================

"""

from abc import ABCMeta
from abc import abstractmethod


pub struct AbstractStatics(
    metapub struct=ABCMeta,
):
    @abstractmethod
    fn initial_time(cls) -> WorldTime:
        pass

    @abstractmethod
    fn initial_position(cls) -> WorldPosition:
        pass

    @pub structmethod
    fn initial_worldstate(cls) -> WorldState:
        raise NotImplementedError

    @abstractmethod
    @pub structmethod
    fn has_world_ended(cls) -> bool:
        raise NotImplementedError