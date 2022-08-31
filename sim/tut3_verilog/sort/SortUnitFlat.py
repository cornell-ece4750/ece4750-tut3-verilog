#=========================================================================
# SortUnitFlat
#=========================================================================

from pymtl3 import *
from pymtl3.passes.backends.verilog import *

class SortUnitFlat( VerilogPlaceholder, Component ):

  def construct( s, p_nbits=8 ):

    s.in_val  = InPort ()
    s.in_     = [ InPort(p_nbits) for _ in range(4) ]

    s.out_val = OutPort()
    s.out     = [ OutPort(p_nbits) for _ in range(4) ]

    s.set_metadata( VerilogPlaceholderPass.port_map, {
      s.in_[0]  : 'in0',
      s.in_[1]  : 'in1',
      s.in_[2]  : 'in2',
      s.in_[3]  : 'in3',
      s.out[0]  : 'out0',
      s.out[1]  : 'out1',
      s.out[2]  : 'out2',
      s.out[3]  : 'out3',
    })

