

## Fractal

`fractal` is a developing spec for a reinforcement learning framework. Currently early prototyping.

It is written with a creative flavor that emphasizes a physical perspective. This is motivated by an interest in computational trinitarianism, as well as some [intuitive ideas](https://github.com/jedhsu/think/blob/main/towards-a-physical-theory-of-consciousness.md).

My strategy to get this going is to architect its features around the well-known implementation of AlphaZero.

Goal at first is to use Python for clarity without caring about speed.

### TODO - blurb on cpt

Talk about architecture decisions and how they are motivated by that perspective. For example, the logic should be constructivist.

### Realizing

The world runs the event loop of `Realizing`. This is the event loop that observes new information as the game takes place.

#### Remarks on Grammatical Tense

Grammatical tense is used to indicate a particular semantics of structs.

- `Operation` represents a concept. These objects contain parameters (immutables).
- `Operating` contains streaming data holding mutable state.
- `Operated` is a result, mostly used for reporting.

For example, the `Evolving` type
* derives its parameters from `Evolution`
* calls `evolve()` in order to run a step
  * which mutates the variables of `Evolving` as an effect
  * and returns an instance of `Evolved` as a result summarizing what happened.

## Mind

The `Mind` is the agent.

Start with the following features:

- `Unicameral`, for a one-person game.
- `Bicameral` for a two-person game.

To represent the learning step, the world is `Evolving`.

### Brain

The `Brain` is the underlying neural network.

- `Cortex`, which inherit from torch's `nn.Sequential` to represent a related section of the brain.
- `Layer`, which inherit from torch's `nn.Module`.

###### Remarks

This section might get moved out later. It feels relatively independent, as it is a library
on top of torch's features.

### Angels

The `Angel`s of the mind `Build` and `Architect` the brain.

To build is to create a new layer, and to architect is to rearrange the architecture of the network.

It is a design goal to have the optionality for the `Build` and `Architect` interfaces to be
_actions of the game_. Then, the act of planning and strategizing is importantly considered
as part of the game itself.

### Demons

The `Demon`s of the mind `Glimpse` and `Interpret` the future.

Demons will be classified into the following types, to represent policies on how to select actions.

- `Naive`: Random selection.
- `Greedy`: Epsilon-greedy.
- `Focused`: Min-max algorithm.
- `Shrewd`: Monte Carlo tree search.
- `Alpha`: The Alpha-zero algorithm.

`Glimpsing` will run the event loop of tree search.

`Interpreting` will run the event loop of constructing `Vision`s, updates of world state and evolutions of the mind based on glimpse.

###### TODO 

- Is Alpha-zero algo in right abstraction layer?

### Daemon

Handles batchifying.

## Fractal

Top-level data model that contains the world and the mind, including the `Training` loop and the `Realizing` loop.

## Remarks

- The folders `_op` contain the interfaces of a struct. This is a personal style preference for modularity.
- The `_prefix` naming scheme of a file indicates association, rather than privacy.

## Acknowledgments

Thanks to Jonathan Laurent's [AlphaZero.jl](https://github.com/jonathan-laurent/AlphaZero.jl), which I'm using substantially as a reference.
