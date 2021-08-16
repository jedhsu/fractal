"""

    *At*

  Abstract type for a parameter schedule, which represents a function from
  nonnegative integers to numbers of type `R`. Subtypes must implement the
  
  `getindex(s::AbstractSchedule, i::Int)` operator.

"""


class At:
    pass
