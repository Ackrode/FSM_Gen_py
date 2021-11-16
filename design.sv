// Output logic
	always @(state, x)
		begin
			case(state)
				A: if(x)
					y = 1'b1
				else
					y = 1'b0
				B: if(x)
					y = 1'b0
				else
					y = 1'b0
				C: if(x)
					y = 1'b1
				else
					y = 1'b0
				D: if(x)
					y = 1'b0
				else
					y = 1'b0
				E: if(x)
					y = 1'b1
				else
					y = 1'b0
				F: if(x)
					y = 1'b0
				else
					y = 1'b0
				default: y = 1'b0;
			endcase
		end
endmodule
