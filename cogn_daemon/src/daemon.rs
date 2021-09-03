

"""
    BatchedOracle(reqc, preprocess=(x->x))


- When invoked on a state, this oracle sends a query to the server identified by
  request channel `reqc`. This call is blocking until every other active worker also
  sends its query.


"""

pub trait Daemon<T> where T: Demon {
    //! A demon which delegates its job to an inference server.

    fn pretransform(&self, transform: ) {};
    //! Applies a preprocessing transform to the passed state before it is
    //! sent to the server as a query.

    fn postransform(&self) {};

    fn delegate(&self) {};
}

pub struct Parallelization{F}
    preprocess: F
}

pub struct Executing {
    listening: Channel,
    speaking: Channel,
}

fn begin() {}
// impl new BatchedOracle(reqchan, preprocess=(x->x))
//     return new{typeof(preprocess)}(preprocess, reqchan, Channel(1))
//   end
// end
