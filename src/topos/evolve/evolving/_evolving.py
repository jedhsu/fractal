"""

    *Evolving*

"""

from dataclasses import dataclass

from mind.cortex import Cortex

@dataclass
class Evolving:
    cortex: Cortex
    placements: Vector[TrainingSample]
    data: NamedTuple # (W, X, A, P, V) tuple obtained after converting `samples`
    Wmean: float
    Hp: float
    batches_stream: Iterator[Batch]

    end |> Util.cycle_iterator |> Iterators.Stateful
    return new(network, samples, params, data, Wmean, Hp, batches_stream,)

