#=========================================================================
# Sort Unit FL Model
#=========================================================================
# Models the functional behavior of the target hardware but not the
# timing.

from copy import deepcopy
from pymtl3 import *

class SortUnitFL( Component ):

  # Constructor

  def construct( s, p_nbits=8 ):

    s.in_val = InPort ()
    s.in_    = [ InPort (p_nbits) for _ in range(4) ]

    s.out_val = OutPort()
    s.out     = [ OutPort(p_nbits) for _ in range(4) ]

    @update_ff
    def block():
      s.out_val <<= s.in_val
      for i, v in enumerate( sorted( s.in_ ) ):
        s.out[i] <<= v

  # Line tracing

  def line_trace( s ):

    in_str = '{' + ','.join(map(str,s.in_)) + '}'
    if not s.in_val:
      in_str = ' '*len(in_str)

    out_str = '{' + ','.join(map(str,s.out)) + '}'
    if not s.out_val:
      out_str = ' '*len(out_str)

    return f"{in_str}|{out_str}"
