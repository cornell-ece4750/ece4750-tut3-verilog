#=========================================================================
# GCD Unit RTL Model
#=========================================================================

from pymtl3 import *
from pymtl3.passes.backends.verilog import *
from pymtl3.stdlib.stream.ifcs import IStreamIfc, OStreamIfc

#=========================================================================
# GCD Unit RTL Model
#=========================================================================

class GcdUnit( VerilogPlaceholder, Component ):
  def construct( s ):
    s.istream = IStreamIfc( Bits32 )
    s.ostream = OStreamIfc( Bits16 )

