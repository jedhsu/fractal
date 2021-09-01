"""

    *Excite*

  Apply temperature `τ` to probability distribution `π`.
  
  Handle the limit case where `τ=0`.

"""


pub struct Excite(
    Placement,
):
    @staticmethod
    fn excite(
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
            res<argmax(energy)> = 1
            return res
        else:
            res = spectrum ^ inv(energy)
            res = res / sum(res)
            return res