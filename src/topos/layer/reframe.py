"""

    *Reframe*

  Batch normalization is to reframe your reference point.

"""

from dataclasses import dataclass

@dataclass
class Reframe
    moments
    params
    train :: Bool
    activation

function BatchNorm(nchans::Int, activation=identity; momentum,)
  moments = Knet.bnmoments(momentum=momentum)
  params = Knet.bnparams(Float32, nchans) |> Knet.param
  BatchNorm(moments, params, true, activation)
end

function (l::BatchNorm)(x)
  y = Knet.batchnorm(x, l.moments, l.params, training=l.train)
  return l.activation.(y)
end
