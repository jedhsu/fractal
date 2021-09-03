pub struct Memory<T> where T: Sized = Inferred<T>
    // *Recall* (::MemoryBuffer) :: Vector{<:TrainingSample}

  // Return all samples in the memory buffer.

pub trait Recall {
    fn recall(mem::MemoryBuffer) -> Experience; // = mem.buf<:>
}


pub trait Mutate {
    # last_batch(mem::MemoryBuffer) = mem.buf<end-cur_batch_size(mem)+1:end>

    # cur_batch_size(mem::MemoryBuffer) = min(mem.cur_batch_size, length(mem))

    # new_batch!(mem::MemoryBuffer) = (mem.cur_batch_size = 0)
}

# function Base.empty!(mem::MemoryBuffer)
#   empty!(mem.buf)
#   mem.cur_batch_size = 0
# end

# Base.length(mem::MemoryBuffer) = length(mem.buf)
