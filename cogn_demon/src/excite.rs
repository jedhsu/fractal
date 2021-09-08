//! Calibrates policy in accordance to its parameter.

pub struct Calibrate(
    Placement,
):
    fn calibrate(
        spectrum: Spectrum,
        energy: f64,
    ) {
        if energy == approx(1):
            return spectrum
        elif energy == approx(0):
            res = zeros(
                eltype(spectrum),
                length(spectrum),
            )
            res<argmax(energy)> = 1
            return res
    } else {
        let res = spectrum ^ inv(energy);
        let res = res / sum(res);
        res
    }
