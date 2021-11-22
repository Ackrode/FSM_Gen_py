`timescale 1ns/1ns

module FSM_TB;
reg clk;
reg reset;
reg x;
wire y;
FSM DUT(clk, reset, x, y);
initial begin
$dumpfile("FSM.vcd");
$dumpvars(0,FSM_TB);
$display("*********************************************");
$display(clk = 1'b0; reset = 1'b1; #2);
$display("clk = %b, reset = %b, x = %b, outp = %b", clk, reset, x, outp);
x = 1'b0;  #2
$display("clk = %b, reset = %b, x = %b, outp = %b", clk, reset, x, outp);
x = 1'b0;  #2
$display("clk = %b, reset = %b, x = %b, outp = %b", clk, reset, x, outp);
x = 1'b1;  #2
$display("clk = %b, reset = %b, x = %b, outp = %b", clk, reset, x, outp);
x = 1'b1;  #2
$display("clk = %b, reset = %b, x = %b, outp = %b", clk, reset, x, outp);
x = 1'b0;  #2
$display("clk = %b, reset = %b, x = %b, outp = %b", clk, reset, x, outp);
$finish;
end
always #1 clk = ~clk;
endmodule
