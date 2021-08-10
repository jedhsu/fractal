"""

    *Focus*

"""

mutable struct Dense
  W
  b
  σ
end

function Dense(in::Int, out::Int, σ=identity)
  W = Knet.param(Float32, out, in, atype=Array)
  b = Knet.param0(Float32, out, atype=Array)
  return Dense(W, b, σ)
end

children(c::Dense) = (c.W, c.b, c.σ)

mapchildren(f, c::Dense) = Dense(f(c.W), f(c.b), f(c.σ))

(d::Dense)(x) = d.σ.(d.W * x .+ d.b)
