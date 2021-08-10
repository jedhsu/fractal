"""


    *Topos*

  A topos contains all the models of a mind, including:

  * Mind, the agent.
  * World, the environment.
  * History, the realization.
    - history of contexts will be annoying and probably bottlenecking - do last
  * Glimpse, the interpretation of the future.

"""

from dataclases import dataclass


@dataclass
class Topos:
    # Store (nonterminal) state statistics assuming the white player is to play
    tree: dict[Placing, Place]

    # External oracle to evaluate positions
    demon: MetaDemon

    # Parameters
    gamma: f64  # Discount factor
    cpuct: f64
    noise_ϵ: f64
    noise_α: f64
    prior_temperature: f64

    # Performance statistics
    total_simulations: Int64
    total_nodes_traversed: Int64

    # Game specification
    physics: Physics
