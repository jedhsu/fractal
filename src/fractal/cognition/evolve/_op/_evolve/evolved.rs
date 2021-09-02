\\\!

    *Evolved*

\\\!

from datapub structes import datapub struct

from .optimized import Optimized


@datapub struct
pub struct Evolved(
    Optimized,
):
    demon_entropy: f64
    brain_entropy: f64


fn evolution_status(
    tr: Trainer,
    samples,
):