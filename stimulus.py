def stimulus(module, states):
    table='state_table.txt'
    # get_info(table)

    # print(states['futures_states'])
    keys=states.keys()
    key=list(keys)
    valor=states.get(key[1])
    # print(valor[5][1])
    


    for j in range(0,len(valor)):
        for i in range(0,2):
            if valor[j][i]=='A':
                valor[j][i]=0
            elif valor[j][i]=='B':
                valor[j][i]=1
            elif valor[j][i]=='C':
                valor[j][i]=2
            elif valor[j][i]=='D':
                valor[j][i]=3
            elif valor[j][i]=='E':
                valor[j][i]=4
            elif valor[j][i]=='F':
                valor[j][i]=5
            elif valor[j][i]=='G':
                valor[j][i]=6
            else:
                print("fail")


    i=0
    j=0
    count=0
    val=[]
    val1=[]
    x=[]

    for t in range(0,9):
        val.append(valor[j][i])
        v=len(val)-1
        val1.append(val[v])
        
        if len(val)-1>0:
            for l in range(0,len(val)):   
                if val[l]==val[v]:
                    count=count+1
        x.append(i)
        
        if count>1:
            val1.pop()
            val.pop()
            x.pop()
            if i==0:
                i=1
            else:
                i=0
            v=len(val)-1
            j=val[v]
        else:
            j=val[v]
        count=0
    print(x)

    testbench_stimulus = []
    f = open(module+"_TB.sv",'a')
    testbench_stimulus.append("$display(\"*********************************************\");")
    testbench_stimulus.append("clk = 1'b0; reset = 1'b1; #2")
    testbench_stimulus.append("$display(\"clk = %b, reset = %b, x = %b, outp = %b\", clk, reset, x, y);")
    testbench_stimulus.append("reset = 1'b0; ")
    for i in range(0,len(x)):
        testbench_stimulus.append("x = 1'b"+str(x[i])+";  #2")
        testbench_stimulus.append("$display(\"clk = %b, reset = %b, x = %b, y = %b\", clk, reset, x, y);")

    testbench_stimulus.append("$finish;")
    testbench_stimulus.append("end")
    testbench_stimulus.append("always #1 clk = ~clk;")
    testbench_stimulus.append("endmodule")
        
    for line in testbench_stimulus:
        f.write(line+'\n')
    f.close()