
pub trait Imagine {
    fn imagine( &self, world: World, on_imagined: Callable);
    //! This is simulate.

    fn imagine_in_parallel( &self, world: World, on_imagined: Callable);
    //! This is distributed simulate.
}
