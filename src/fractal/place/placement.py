from dataclasses import dataclass


@dataclass
class Place:
    placements: Vector[Placement]
    value: f32
