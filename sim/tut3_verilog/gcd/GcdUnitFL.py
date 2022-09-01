#=========================================================================
# GCD Unit FL Model
#=========================================================================

from math import gcd

from pymtl3 import *
from pymtl3.stdlib.stream.ifcs import IStreamIfc, OStreamIfc
from pymtl3.stdlib.stream      import IStreamDeqAdapterFL, OStreamEnqAdapterFL

#-------------------------------------------------------------------------
# GcdUnitFL
#-------------------------------------------------------------------------

class GcdUnitFL( Component ):

  # Constructor

  def construct( s ):

    # Interface

    s.istream = IStreamIfc( Bits32 )
    s.ostream = OStreamIfc( Bits16 )

    # Queue Adapters

    s.istream_q = IStreamDeqAdapterFL( Bits32 )
    s.ostream_q = OStreamEnqAdapterFL( Bits16 )

    s.istream //= s.istream_q.istream
    s.ostream //= s.ostream_q.ostream

    # FL block

    @update_once
    def block():
      if s.istream_q.deq.rdy() and s.ostream_q.enq.rdy():
        msg = s.istream_q.deq()
        s.ostream_q.enq( gcd( msg[16:32], msg[0:16] ) )

  # Line tracing

  def line_trace( s ):
    return f"{s.istream}(){s.ostream}"

