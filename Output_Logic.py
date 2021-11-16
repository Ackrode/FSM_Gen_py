from get_info import *

module, inputs, outputs, states = get_info("state_table.txt")
Output_Logic = []
f = open("design.sv", 'w')
Output_Logic.append("// Output logic")
Output_Logic.append("\talways @(state, " + inputs["name"][2] + ")")
Output_Logic.append("\t\tbegin")
Output_Logic.append("\t\t\tcase(state)")
for i in range(0, len(states["presentes_states"]), 1):
    Output_Logic.append("\t\t\t\t" + states["presentes_states"][i] + ": " + "if(" + inputs["name"][2] + ")")
    Output_Logic.append("\t\t\t\t\t" + outputs["name"][0] + " = 1'b" + states["output"][i][1])
    Output_Logic.append("\t\t\t\telse")
    Output_Logic.append("\t\t\t\t\t" + outputs["name"][0] + " = 1'b" + states["output"][i][0])            
Output_Logic.append("\t\t\t\tdefault: " + outputs["name"][0] + " = 1'b0;")
Output_Logic.append("\t\t\tendcase")
Output_Logic.append("\t\tend")
Output_Logic.append("endmodule")
for line in Output_Logic:
    f.write(line+'\n')
f.close()