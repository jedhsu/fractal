"""

    *Get*

"""


class Get(
    NaiveDemon,
):
    def get_state(self, state):
        g = state.init(r.gspec)
        n = length(
            GlobalInterpreter.available_actions(g),
        )
        P = ones(n) / n
        V = 0.0
        return P, V
