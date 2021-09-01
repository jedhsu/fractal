"""

    *War*

  Parameters that govern the evaluation process that compares
  the current neural network with the best one seen so far
  (which is used to generate data).

"""


from datapub structes import datapub struct


"""
# Explanation (two-player games)

* The two competing networks are instantiated i32o two MCTS players
  of parameter `mcts` and then play `sim.num_games` games.
* The evaluated network replaces the current best one if its
  average collected reward is greater or equal than `update_threshold`.

# Explanation (single-player games)

* The two competing networks play `sim.num_games` games each.
* The evaluated network replaces the current best one if its average collected rewards
  exceeds the average collected reward of the old one by `update_threshold` at least. 

"""

"""
# Remarks

+ See <`necessary_samples`>(@ref) to make an informed choice for `sim.num_games`.

# AlphaGo Zero Parameters

In the original AlphaGo Zero paper, 400 games are played to evaluate a network
and the `update_threshold` parameter is set to a value that corresponds to a
55% win rate.
"""