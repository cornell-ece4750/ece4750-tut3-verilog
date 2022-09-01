//========================================================================
// Registered Incrementer
//========================================================================
// This is a simple example of a module for a registered incrementer
// which combines a positive edge triggered register with a combinational
// +2 incrementer. We use flat register-transfer-level modeling.

`ifndef TUT3_VERILOG_REGINCR_REG_INCR_V
`define TUT3_VERILOG_REGINCR_REG_INCR_V

// You will need to uncomment this when you explore line tracing.
//
// `include "vc/trace.v"

module tut3_verilog_regincr_RegIncr
(
  input  logic       clk,
  input  logic       reset,
  input  logic [7:0] in_,
  output logic [7:0] out
);

  // Sequential logic

  logic [7:0] reg_out;
  always @( posedge clk ) begin
    if ( reset )
      reg_out <= 0;
    else
      reg_out <= in_;
  end

  // ''' TUTORIAL TASK '''''''''''''''''''''''''''''''''''''''''''''''''''
  // This model is incomplete. As part of the tutorial you will insert
  // combinational logic here to model the incrementer logic.
  // '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

  // You will need to uncomment this when you explore line tracing.
  //
  // `ifndef SYNTHESIS
  //
  // logic [`VC_TRACE_NBITS-1:0] str;
  // `VC_TRACE_BEGIN
  // begin
  //   $sformat( str, "%x (%x) %x", in_, reg_out, out );
  //   vc_trace.append_str( trace_str, str );
  // end
  // `VC_TRACE_END
  //
  // `endif /* SYNTHESIS */

endmodule

`endif /* TUT3_VERILOG_REGINCR_REG_INCR_V */
