import math      
def get_state(path, module, inputs, outputs, states):
    Output_Logic = []
    inputs3 = inputs.get("size")
    f = open(path, 'w')
    ### Declaration of module
                                ##Aqui iria el FSM:Abajo
    Output_Logic.append("module "+module.get('name')+" ("+inputs["name"][0]+","+inputs["name"][1]+","+inputs["name"][2]+","+outputs["name"][0]+");")
    Output_Logic.append("\t"+"input"+" "+ inputs3[2]+" "+inputs["name"][1]+","+inputs["name"][0]+","+inputs["name"][2]+";")
    Output_Logic.append("\t"+"output reg"+" "+ inputs3[2]+"" +" "+outputs["name"][0]+";")
    Output_Logic.append("   ")

    ### Part of reg
    x = len (states["presentes_states"])   
    answer = math.log(x, 2)
    reg1 = math.ceil(answer)
    reg2 = reg1 - 1
    Output_Logic.append("\t"+"reg ["+str(reg2)+":"+"0] "+"state;")
    Output_Logic.append("\t"+"reg ["+str(reg2)+":"+"0] "+"next_state;")
    Output_Logic.append("   ")

    ## state codification

    for i in range(0, len(states["presentes_states"]), 1):
        Output_Logic.append ("\t"+"parameter"+" "+states["presentes_states"][i]+" "+"="+ str(i)+";")
    Output_Logic.append("   ")          
    Output_Logic.append("\t"+"initial begin")
    Output_Logic.append("\t\t"+"state ="+states["presentes_states"][0]+";")
    Output_Logic.append("\t"+"end")
    Output_Logic.append("   ")

    ## State register
    Output_Logic.append("\t"+"always @(posedge"+" "+inputs["name"][0]+","+"posedge"+" "+inputs["name"][1]+")")
    Output_Logic.append("\t\t"+"begin")
    Output_Logic.append("\t\t\t"+"state <="+states["presentes_states"][0]+";")
    Output_Logic.append("\t\t"+"else")
    Output_Logic.append("\t\t\t"+"state <= next_state;")
    Output_Logic.append("\t\t"+"end")

    for line in Output_Logic:
        f.write(line+'\n')
    f.close()