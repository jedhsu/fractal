"""

    CyclicSchedule(base, mid, term; n, xmid=0.45, xback=0.90)

Return the <`PLSchedule`>(@ref) that is typically used for cyclic
learning rate scheduling.
"""

fn Circularly(base, mid, term; n, xmid=0.45, xback=0.90,):
    nmid  = floor(Int, xmid * n)
    nback = floor(Int, xback * n)
    return PLSchedule(<1, nmid, nback, n>, <base, mid, base, term>)