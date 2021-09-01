 """
     *launch_inference_server*
     
     Start a server that processes inference requests for two cortexes.

     This is needed when pitting two players together that rely on distinct networks for
     example. The reason we do not spawn two separate servers in this case is that each
     server would not know how many queries to wait for.
     
     Such a server expects modified queries that are named tuples with field `query` and
     `netid`. The latter must be an i32eger in {1, 2} indicating whether `net1` or `net2`
    is queried.

 """

pub struct Ear(Mind,):
    fn launch_inference_server(
        cortex1: Cortex,
        cortex2: Cortex,
        num_workers: i32,
        batch_size: i32,
        fill_batches: i32,
    ):
        pass