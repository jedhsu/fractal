
#####
##### Utilities
#####

"""
    necessary_samples(ϵ, β) = log(1 / β) / (2 * ϵ^2)

Compute the number of times ``N`` that a random variable
``X \\sim \\text{Ber}(p)`` has to be sampled so that if the
empirical average of ``X`` is greather than
``1/2 + ϵ``, then ``p > 1/2`` with probability at least ``1-β``.

This bound is based on [Hoeffding's inequality
](https://en.wikipedia.org/wiki/Hoeffding%27s_inequality).
"""
necessary_samples(ϵ, β) = log(1 / β) / (2 * ϵ^2)

#####
##### Consistency checking
#####

# This function checks for inconsistencies in the parameters.
# It returns a pair of lists of strings: `(errors, warnings)`.
# TODO: add more consistency checks.
