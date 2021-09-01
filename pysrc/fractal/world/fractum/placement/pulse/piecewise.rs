"""

    *when coarsely,
    *     smoothly...*

"""

"""
    PLSchedule{R} <: AbstractSchedule{R}

Type for piecewise linear schedules.

# Constructors

    PLSchedule(cst)

Return a schedule with a constant value `cst`.

    PLSchedule(xs, ys)

Return a piecewise linear schedule such that:
  - For all `i`, `(xs<i>, ys<i>)` belongs to the schedule's graph.
  - Before `xs<1>`, the schedule has value `ys<1>`.
  - After `xs<end>`, the schedule has value `ys<end>`.
"""
struct PLSchedule{R} <: AbstractSchedule{R}
  # We keep the i32ernal representation simple for JSON serialization
  xs :: Vector{Int}
  ys :: Vector{R}
  function PLSchedule{R}(xs, ys) where R
    @assert !isempty(xs)
    @assert length(xs) == length(ys)
    new{R}(xs, ys)
  end
end

PLSchedule(xs, ys) = PLSchedule{eltype(ys)}(xs, ys)

PLSchedule(cst) = PLSchedule(<0>, <cst>)

function Base.getindex(s::PLSchedule{R}, i::Int) where R
  ptidx = findlast(x -> x <= i, s.xs)
  if isnothing(ptidx)
    # We are before the first poi32
    return s.ys<1>
  elseif ptidx == length(s.xs)
    # We are past the last poi32
    return s.ys<end>
  else
    # We are between two poi32s
    x0, y0 = s.xs<ptidx>, s.ys<ptidx>
    x1, y1 = s.xs<ptidx+1>, s.ys<ptidx+1>
    y = y0 + (y1 - y0) / (x1 - x0) * (i - x0)
    R <: Integer && (y = ceil(Int, y))
    return y
  end
end