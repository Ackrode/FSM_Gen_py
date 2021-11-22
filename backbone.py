def convert(s):
    # initialization of string to ""
    new = "" 
    # traverse in the string 
    for x in s:
        # For the last item in the string don't add a comma
        if x==s[-1]:
            new+=x
        else:
            new =new+ x +', '  
    return new
# Get the number of input bits
def get_n(inputs=[]):
    n=0
    if inputs:
# Iterate through the inputs
        for i in inputs.get('size'):
            if len(i)==2:
                n=n+int(i[0])-int(i[1])+1
            else:
                n=n+1

    return n
def backbone(inputs=[], outputs=[],inouts=[], module=''): 


    testbench=[]
    #
    with open(module+"_TB.sv",'w') as file:
        testbench=["`timescale 1ns/1ns\n", 'module '+module +'_TB;']
        j=0
        # if inputs is not empty
        if inputs:
            # Iterate through the inputs and append it with their bus size
            for name in inputs.get('name'):
                # If the inputs.get('name') size is 1, then the input is a single bit
                if len(inputs.get('size')[j])==2:
                    testbench.append('reg'+' ['+inputs.get('size')[j][0]+':' +inputs.get('size')[j][1]+'] '  + name +';')
            
                else:
                    testbench.append('reg '+ name +';')
                j=j+1
        j=0
        if outputs:
            for name in outputs.get('name'):
                if len(outputs.get('size')[j])==2:
                    testbench.append('wire'+' ['+outputs.get('size')[j][0]+':' +outputs.get('size')[j][1]+'] '  + name +';')
                        
                else:
                    testbench.append('wire '+ name +';')
                j=j+1
        j=0
        if inouts:
            for name in inouts.get('name'):
                if len(inouts.get('size')[j])==2:
                    testbench.append('wire'+' ['+inouts.get('size')[j][0]+':' +inouts.get('size')[j][1]+'] '  + name +';')
                else:
                    testbench.append('wire '+ name +';')
                j=j+1
        j=0
        # Convert the name dict to a string
        intputL=convert(inputs.get('name'))
        outputL=convert(outputs.get('name'))
        if inouts:
            inoutL=convert(inouts.get('name'))
        # Append the converted items to the testbench
        # If the inout is not empty then add the inout to the DUT 
        if inouts:
            testbench.append(module+' DUT('+intputL+', '+outputL+', '+inoutL+');')
        else:
            testbench.append(module+' DUT('+intputL+', '+outputL+');')
        testbench.append('initial begin')
        testbench.append('$dumpfile("'+module+'.vcd");')
        testbench.append('$dumpvars(0,'+module+'_TB);')
        # Write the testbench to the file
        for line in testbench:
            file.write(line+'\n')
