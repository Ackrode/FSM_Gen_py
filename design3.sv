module FSM (clk,reset,x,y);
	input [0:0] reset,clk,x;
	output reg [0:0] y;
   
	reg [2:0] state;
	reg [2:0] next_state;
   
	parameter A =0;
	parameter B =1;
	parameter C =2;
	parameter D =3;
	parameter E =4;
	parameter F =5;
   
	initial begin
		state =A;
	end
   
	always @(posedge clk,posedge reset)
		begin
			state <=A;
		else
			state <= next_state;
		end
