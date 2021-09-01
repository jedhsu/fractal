//! Awe is the AlphaZero demon.

pub struct Awe {

}

| Parameter              | Type                         | Default             |
|:-----------------------|:-----------------------------|:--------------------|
| `num_iters_per_turn`   | `Int`                        |  -                  |
| `gamma`                | `Float64`                    | `1.`                |
| `cpuct`                | `Float64`                    | `1.`                |
| `temperature`          | `AbstractSchedule{Float64}`  | `ConstSchedule(1.)` |
| `dirichlet_noise_ϵ`    | `Float64`                    |  -                  |
| `dirichlet_noise_α`    | `Float64`                    |  -                  |
| `prior_temperature`    | `Float64`                    | `1.`                |

# Explanation

An MCTS player picks an action as follows. Given a game state, it launches
`num_iters_per_turn` MCTS iterations, with UCT exploration constant `cpuct`.
Rewards are discounted using the `gamma` factor.

Then, an action is picked according to the distribution ``π`` where
``π_i ∝ n_i^{1/τ}`` with ``n_i`` the number of times that the ``i^{\\text{th}}``
action was visited and ``τ`` the `temperature` parameter.

It is typical to use a high value of the temperature parameter ``τ``
during the first moves of a game to increase exploration and then switch to
a small value. Therefore, `temperature` is am <`AbstractSchedule`>(@ref).

For information on parameters `cpuct`, `dirichlet_noise_ϵ`,
`dirichlet_noise_α` and `prior_temperature`, see <`MCTS.Env`>(@ref).
