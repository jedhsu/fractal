
    def get_state(self):
        g = GlobalInterpreter.init(r.gspec, state)
        n = length(GlobalInterpreter.available_actions(g))
        P = ones(n) / n
        V = 0.0
        return P, V
