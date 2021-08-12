## Fractal

`fractal` is a developing spec for a reinforcement learning framework.

It is written with a creative flavor of computational trinitarianism based on some [deeper intuitions](https://github.com/jedhsu/think/blob/main/towards-a-physical-theory-of-consciousness.md).

My strategy to get this going is to architect its features around the well-known implementation of AlphaZero.

## World

The `World` encapsulates the environment.

- `Nature` holds all static variables.
- `Dynamics` holds all dynamic state.

A design goal is to make the data model for the rules of the game be dynamical
This represents that certain "rules of the game" can change, and in fact might
be the primary parameters of change for an unsupervised learner.

### Fractum

An environment state is a `Fractum`. It consists of
- a `Quantum`, a discrete quantity,
- a `Place` describing its position in some generic spacetime,
- a `Spectrum`, a probability distribution describing its near-future placement.

###### TODO

- Read quantum mechanics to see if rigorously compares.

### Realizing

The world runs the event loop of `Realizing`. This is the event loop that observes new information as the game takes place.

#### Remarks on Grammatical Tense

Grammatical tense is used to indicate a particular semantics of an object.

- `Operation` is a concept. These hold the parameters, the associated types, of an object.
- `Operator` is a type.
- `Operating` is a function holding computation steps, as well as the event loop representing the "present time".
- `Operate` is an async function that returns an await, as asynchronous functions abstract time from computation.
- `Operated` is a value instantiated by the type Operator.

Summary metrics use past tense like `Awakened`, to appropriately describe its temporal state.

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