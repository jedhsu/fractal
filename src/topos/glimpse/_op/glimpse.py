"""

    *Glimpse*

  Runs a single Monte-Carlo tree search simulation, updating
  all traversed placements.

  Mutates the global topos.

  Returns the estimated Q-value for the current cortex.

"""

from math import sqrt


class Glimpse(Analyze):
    def glimpsing(
        cls,
        topos: Topos,
        spacetime: Spacetime,
        eta,
        root=true,
    ) -> Qvalue:
        state = GI.current_state(spacetime)
        actions = GI.available_actions(spacetime)
        info, new_node = state_info(env, state)

        if new_node:
            return info.Vest
        else:
            if root:
                epsilon = nature.noise_epsilon
            else:
                epsilon = 0

        scores = cls.upper_confidence_bounds(
            info,
            env.cpuct,
            epsilon,
            eta,
        )
        action_id = argmax(scores)
        action = actions[action_id]

        spacetime.flow(placement)
        wr = GI.white_reward(game)
        if spacetime.is_dawn():
            r = wr
        else:
            r = -wr

        shall_cortex_change = wp != GI.white_playing(game)

        qnext = glimpsing(
            env,
            game,
            η=η,
            root=false,
        )

        if shall_cortex_change:
            qnext = -qnext

        qvalue = r + topos.gamma * qnext

        cls.update(
            env,
            state,
            action_id,
            q,
        )
        env.total_nodes_traversed += 1
        return
