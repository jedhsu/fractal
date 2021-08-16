"""

    *Processing*

  Memory buffer.

"""

from fractal.world import Nature

from dataclasses import dataclass


@dataclass
class Processing:
    nature: Nature
    ring: RingBuffer[Observation]
    batch_size: int
