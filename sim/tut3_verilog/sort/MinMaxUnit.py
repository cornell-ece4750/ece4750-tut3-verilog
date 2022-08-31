#=========================================================================
# MinMaxUnit
#=========================================================================
# This module takes two inputs, compares them, and outputs the larger
# via the "max" output port and the smaller via the "min" output port.

from pymtl3 import *
from pymtl3.passes.backends.verilog import *

class MinMaxUnit( VerilogPlaceholder, Component ):
  def construct( s, p_nbits ):
    s.in0     = InPort ( p_nbits )
    s.in1     = InPort ( p_nbits )
    s.out_min = OutPort( p_nbits )
    s.out_max = OutPort( p_nbits )

