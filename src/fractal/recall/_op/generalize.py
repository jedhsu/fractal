"""

    *Generalize*

"""


class Generalize(Recall):
    def generalize(
        self,
        sample,
        (symstate, aperm),
    ):
        mask = GlobalInterpreter.actions_mask(
            GlobalInterpreter.init(gspec, sample.s),
        )
        symmask = GlobalInterpreter.actions_mask(
            GlobalInterpreter.init(gspec, symstate)
        )

        π = zeros(eltype(sample.π), length(mask))
        π[mask] = sample.π
        π = π[aperm]
        assert π[.~symmask] == 0
        π = π[symmask]
        return typeof(sample)(symstate, π, sample.z, sample.t, sample.n,)
