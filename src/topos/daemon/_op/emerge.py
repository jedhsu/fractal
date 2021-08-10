"""

    *Emerge*

"""

from types import FunctionType as Function as Process

class Emerge(
    Topos,
):
    def emerge(self):
        reqc = launch_inference_server(western[2])
        make2 = Batchifier.BatchedOracle(reqc)
        # return zipthunk(ret_oracle(eastern[1]), make2)send_done!(reqc)

    def emerge_west(
        self,
        west,
        **kwargs,
    ):
        reqc = launch_inference_server(
            self[1],
        )
        make1 = Batchifier.BatchedOracle(reqc)
        # return zipthunk(make1, ret_oracle(os[2])), send_done!(reqc)

# """
#     batchify_oracles(oracles; num_workers, batch_size, fill_batches)

# Take some oracles, launch a server to call them by batches if needed and return a pair
# of functions to be called by each concurrent worker:

#   - A `spawn_oracles()` function that expects no argument and returns `BatchedOracle`s
#     to be used by the worker.
#   - A `done!()` function to be called when the worker is finished and won't make anymore
#     query.

# The `oracles` argument can be either an oracle or a pair of oracles. If one of the two
# oracles at least is a neural network, an inference server will be launched using 
# [`launch_inference_server`](@ref).
# """
def batchify_oracles():
    return None

"""
General tense is the call of a present tense.
"""

def invoke(daemon: daemon):
    def invoking():
        return daemon
    return invoking

def wait() -> Process:
    def waiting() -> None:
        return
    return waiting

def speak(thought) -> Process:
    def speaking():
        pass
        # send_done!(reqc) = () -> Batchifier.client_done!(reqc)

def evaluating(f1, f2) -> Process:
    def evaluating():
        return f1(), f2()
    
    return evaluating






# function batchify_oracles(os::Tuple{<:Any, <:Any}; kwargs...)
#   return zipthunk(ret_oracle(os[1]), ret_oracle(os[2])), do_nothing!
# end
