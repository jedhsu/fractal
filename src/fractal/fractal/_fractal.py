"""


    *Fractal*

  * Mind, the agent.
  * World, the environment.
  * Realizing, the realizat.
    - history of contexts will be annoying and probably bottlenecking - do later
  * Glimpsing, the interpretation of the future.

  # [TODO] move realizing glimpsing?

"""

from dataclasses import dataclass

f64 = float
u64 = int


@dataclass
class Fractal:
    # Store (nonterminal) state statistics assuming the white player is to play
    tree: dict[Placing, Place]

    # External oracle to evaluate positions
    demon: Demon

    # Parameters
    gamma: f64  # Discount factor
    cpuct: f64
    noise_ϵ: f64
    noise_α: f64
    prior_temperature: f64

    # Performance statistics
    total_simulations: i64
    total_nodes_traversed: i64

    # Game specification
    physics: Physics
