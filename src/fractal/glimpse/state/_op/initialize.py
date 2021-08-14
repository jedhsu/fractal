from math import approx


class Initialize(State):
    @classmethod
    def initialize(
        cls,
        probability,
        value,
        prior_temperature,
    ):
        P = Util.apply_temperature(P, prior_temperature)
        stats = [ActionStats(p, 0, 0) for p in P]
        return StateInfo(stats, V)

    """
    apply_temperature

    Apply temperature `τ` to probability distribution `π`.
    Handle the limit case where `τ=0`.

    """

    @staticmethod
    def excite(
        spectrum: Spectrum,
        energy: float,
    ):
        if energy == approx(1):
            return spectrum
        elif energy == approx(0):
            res = zeros(
                eltype(spectrum),
                length(spectrum),
            )
            res[argmax(energy)] = 1
            return res
        else:
            res = spectrum ^ inv(energy)
            res = res / sum(res)
            return res
