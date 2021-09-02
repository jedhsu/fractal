//! A naive min-max tree search algorithm.
//!
//! A simple implementation of the minmax tree search algorithm, to be used as
//! a baseline against AlphaZero.
//!



amplify(r) = iszero(r) ? r : Inf * sign(r)

fn minmax(player, game, actions, depth)
  return argmax(<qvalue(player, game, a, player.depth) for a in actions>)

pub struct Acumen {
    //! `Acumen` applies the min-max tree search algorithm.

    depth: f64,
    //! The minmax player explores the game tree exhaustively at depth `depth`
    //! to build an estimate of the Q-value of each available action. Then, it
    //! chooses an action as follows:
    //!
    //!   + If there are winning moves (with value `Inf`), one of them is picked
    //!   uniformly at random.
    //!
    //!   + If all moves are losing (with value `-Inf`), one of them is picked
    //!   uniformly at random.

    temperature: f64,
    //! If the temperature `τ` is zero, a move is picked uniformly among those
    //! with maximal Q-value (there is usually only one choice).
    //!
    //! If the temperature `τ` is nonzero, the probability of choosing
    //! action ``a`` is proportional to ``e^{\\frac{q_a}{Cτ}}`` where ``q_a`` is the
    //! Q value of action ``a`` and ``C`` is the maximum absolute value of all
    //! finite Q values, making the decision invariant to rescaling of
    //! <`GameInterface.heuristic_value`>(@ref).

    shall_amplify_rewards: bool,
    //! If the `amplify_rewards` option is set to true, every received positive reward
    //! is converted to ``∞`` and every negative reward is converted to ``-∞``.
}

pub trait Acute: Mind {
    //! A mind applying `Acumen`.
    depth;
}


    // MinMax.Player(;depth, amplify_rewards, τ=0.)


////! Benchmark.MinMaxTS(;depth, τ=0.) <: Benchmark.Player
//// # Minmax baseline, which relies on <`MinMax.Player`>(@ref).
//// # \\\!

//pub struct Minimax {
//    depth: i32,
//    amplify_rewards: bool,
//    tau: f64,
//}

//fn new(minimax: Minimax, nature: Nature, brain: Brain) {
//    MinMax.Player { depth: minimax.depth, amplify_rewards: minimax.amplify_rewards, tau: minimax.τ }
//}

impl Minimax {
    fn temperature(
        &self,
        mind: &Mind,
        world: &Realizing,
        depth: i32,
    ):
        //!  Compute state value.

        if GlobalInterpreter.game_terminated(game) {
            0.
        } else if depth == 0 {
            GI.heuristic_value(game)
        } else {
            let qs = <qvalue(player, game, a, depth) for a in GI.available_actions(game)>;
            max(qs)
        }

    fn energy(
        &self,
        mind: &Mind,
        world: &Realizing,
        depth: i32,
        action: Action,
    ) {
        assert!(not world.has_ended());

        let next = world.clone();

        GlobalInterpreter.flow(
            next,
            place,
        )

        let wr = GlobalInterpreter.energy(next);
        let r = GlobalInterpreter.white_playing(game) or wr == -wr;

        if &self.shall_amplify_rewards {
            let r = mind.amplify(r);
        }

        let nextv = cortex(player, next, depth - 1);

        if world.time.at_dawn(game) != world.time.is_dawn(nextv) {
            nextv = -nextv
        }

        r + player.gamma * nextv;
    }
}
