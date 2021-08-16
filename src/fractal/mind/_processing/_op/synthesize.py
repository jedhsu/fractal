"""

    *Synthesize*

"""

from fractal.world import Nature

from .._processing import Processing

class Synthesize(Processing,):
    def synthesize(
        self,
        nature: Nature,
        observed: Observed,
        (symstate, aperm),
    ):
        mask = GlobalInterpreter.actions_mask(
            GlobalInterpreter.init(gspec, sample.s),
        )
        symmask = GlobalInterpreter.actions_mask(
            GlobalInterpreter.init(gspec, symstate)
        )

        spectrum = zeros(eltype(sample.π), length(mask))
        spectrum[mask] = observed.spectrum
        spectrum= spectrum[aperm]
        assert spectrum[.~symmask] == 0
        spectrum = spectrum[symmask]
        return Observed.__class__(symstate, π, sample.z, sample.t, sample.n,)
