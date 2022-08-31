//========================================================================
// RegIncr Ad-Hoc Testing
//========================================================================

`include "RegIncr.v"

module top;

  // Clocking

  logic clk = 1;
  always #5 clk = ~clk;

  // Instaniate the design under test

  logic       reset = 1;
  logic [7:0] in_;
  logic [7:0] out;

  // ''' TUTORIAL TASK '''''''''''''''''''''''''''''''''''''''''''''''''''
  // This simulator script is incomplete. As part of the tutorial you
  // will need to instantiate and connect a RegIncr model here.
  // '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

  // Simulate the registered incrementer

  initial begin

    // Dump waveforms

    $dumpfile("regincr-adhoc-test.vcd");
    $dumpvars;

    // Reset

    #11;
    reset = 1'b0;

    // Cycle 1

    in_ = 8'h01;
    #10;
    $display( " cycle = 1: in = %x, out = %x", in_, out );

    // Cycle 2

    in_ = 8'h13;
    #10;
    $display( " cycle = 1: in = %x, out = %x", in_, out );

    // Cycle 3

    in_ = 8'h25;
    #10;
    $display( " cycle = 1: in = %x, out = %x", in_, out );

    // Cycle 4

    in_ = 8'h37;
    #10;
    $display( " cycle = 1: in = %x, out = %x", in_, out );

    $finish;
  end

endmodule

