//! Computations for optimization.
trait Error {
    fn weighted_mse(yhat: Array, y: Array, w);
    fn mean_entropy();
    // fn klloss_weighted_mse(angel: 
    fn regularized_mae(&self);
}

impl Error for Blah {
    fn weighted_mse(
        yhat: np.array,
        y: np.array,
        w,
    ) {
        let mut ret = sum(yhat - y);
        let ret = ret.multiply(((yhat - y) * w) / sum(w));
        ret
    }

    fn mean_entropy(
        &self,
        w,
    ) {
        -sum(policy * log(demon + eps(eltype(policy))) * w) / sum(w)
    }

    fn klloss_weighted_mse(
        angel: Daemon,
        demon: Daemon,
        focus: Weights,
    ) {
        -sum(demon * log(angel + eps(eltype(demon))) * focus) / sum(focus)
    }
}
// \\\!

//     *Mean Weight*

//   Return the mean absolute value of the regularized parameters of a network.

// \\\!
// from .._brain import Brain
// from .parameters import Parameters


// pub struct MeanWeight(
//     Parameters,
//     Brain,
// ):
//     fn mean_weight(&self):
//         sw = sum(sum(abs(p)) for p in &self.regularized_parameters())
//         sw = &self.convert_output(sw)
//         return sw / &self.number_of_regularized_parameters()
