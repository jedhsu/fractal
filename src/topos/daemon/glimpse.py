
"""

    *Glimpse*

  Play a series of games using a given [`Simulator`](@ref).

"""

class Glimpse(Vision):
    def glimpsing(
        self,
        vision: Vision,
        spacetime: Spacetime,
        game_simulated
    ):

      oracles = simulator.make_oracles()
      spawn_oracles, done =
        batchify_oracles(oracles; p.num_workers, p.batch_size, p.fill_batches)
      return Util.mapreduce(1:p.num_games, p.num_workers, vcat, []) do
        oracles = spawn_oracles()
        player = simulator.make_player(oracles)
        worker_sim_id = 0
        # For each worker
        function simulate_game(sim_id)
          worker_sim_id += 1
          # Switch players' colors if necessary: "_pf" stands for "possibly flipped"
          if isa(player, TwoPlayers) && p.alternate_colors
            colors_flipped = sim_id % 2 == 1
            player_pf = colors_flipped ? flipped_colors(player) : player
          else
            colors_flipped = false
            player_pf = player
          end
          # Play the game and generate a report
          trace = play_game(gspec, player_pf, flip_probability=p.flip_probability)
          report = simulator.measure(trace, colors_flipped, player)
          # Reset the player periodically
          if !isnothing(p.reset_every) && worker_sim_id % p.reset_every == 0
            reset_player!(player)
          end
          # Signal that a game has been simulated
          game_simulated()
          return report
        end
        return (process=simulate_game, terminate=done)

      # Keyword Arguments

      - `game_simulated` is called every time a game simulation is completed
        (with no arguments)

    # Return

    Return a vector of objects computed by `simulator.measure`.
