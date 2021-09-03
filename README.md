

## cogn

An experimental reinforcement learning framework designed from a perspective of [computational](https://ncatlab.org/nlab/show/computational+trilogy)
[trinitarianism](https://existentialtype.wordpress.com/2011/03/27/the-holy-trinity/).

### Motivation

Cogn is motivated by the hypothesis that cognition is a physical a developed theory of cognition cannot be
abstracted away from physics for it to possess a certain kind of meaning. TODO
footnote on intuiniitionistic math.

For both man and
machine, cognition for both
and machine is a physical process "embedded in the flow of time".

Expand on this somewhere else on the physical process. Give thought experiment on the experience of
math, and analogize.

I believe that the ideas in computational trinitarianism are fundamental to this
issue. 

This means that it is critical to address thatk


The flow of time cannot be abstracted away. In practice, this means that we
must 

Cogn is designed to implement the following two features to be first-class {

    1. A physical model of space & time based on quantum mechanics. States are points in space.
       
    1. Extension of modifications of a neural network as a first-class action. This is
       obvious. The degree

    2. States are framed.


#### Mutation

    It is clear that we want the action space to include mutations of the
    underlying neural network. The challenge is how to specify

Yet the more I think about this, it is deeply relevant.

To go from 'Train' to 'Evolve', I think the following must be solved {
    
}

These 


  



### Motivation

Pronounced as 'cognition'.

### Features

Cogn separates itself from existing explore the

  +  Develop RL maturity in Rust, where it currently lags.

  
In the long-term, rather than to do it in Rust.



###### TODO
research a bit more on existing frameworks. gym, deepmind's something, rsrl, any
else?

### Architecture


trilogy](, written in Rust.

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

###### TODO 

- Is Alpha-zero algo in right abstraction layer?

### Daemon

Handles batchifying.

## Fractal

Top-level data model that contains the world and the mind, including the `Training` loop and the `Realizing` loop.

## Remarks

- The folders `_op` contain the interfaces of a struct. This is a personal style preference for modularity.
- The `_prefix` naming scheme of a file indicates association, rather than privacy.

## References & Acknowledgments

Harper.

Corfield.


Thanks to Jonathan Laurent's
[AlphaZero.jl](https://github.com/jonathan-laurent/AlphaZero.jl), which I've
been using heavily as a reference.
