
from dataclasses import dataclass

@dataclass
class SkipConnection:
    block
    connection

children(c::SkipConnection) = (c.block,)

function mapchildren(f, c::SkipConnection)
  SkipConnection(f(c.block), c.connection)
end

function (skip::SkipConnection)(input)
  skip.connection(skip.block(input), input)
end
