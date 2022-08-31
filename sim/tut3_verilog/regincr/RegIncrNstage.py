#=========================================================================
# RegIncrNstage
#=========================================================================
# Registered incrementer that is parameterized by the number of stages.

from pymtl3 import *
from pymtl3.passes.backends.verilog import *

class RegIncrNstage( VerilogPlaceholder, Component ):
  def construct( s, p_nstages=2 ):
    s.in_ = InPort ( 8 )
    s.out = OutPort( 8 )


