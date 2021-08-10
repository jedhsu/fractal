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
        if isone(energy):
            return spectrum
        elif iszero(energy):
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
