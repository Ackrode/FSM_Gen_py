import re

def text_match(pattern,text):
        if re.search(pattern,text):
                return 1 
        else:
                return 0

def get_info(text):
    ###read filed
    filed=open(text,'rt', encoding='utf-8')
    file=filed.read()
    filed.close()
    
                                 ###patterns[0]=module, inputs,output, patterns[1]=present states, patterns[2]=future states, patterns[3]=states_outputs 
    patterns=[r'(module|input|output)[\s]+([^;)]+)*',r'(\b[A-Z])([\,])',r'(\b[A-Z])([\-])',r'\-([0-1]*)',r'([\[\]])']
    type=['module','input','output','error']

    entityinf=re.findall(patterns[0],file)
    edopp=re.findall(patterns[1],file)
    edofp=re.findall(patterns[2],file)
    state_outputp=re.findall(patterns[3],file)
    ncomb=2                           ##number of combinations
    inputs=[]
    size_inputs=[]
    outputs=[]
    size_outputs=[]
    
##***********************get information of the entity****************************************
    for i in  entityinf:
        list_in=[]
        n=[]
        n1=[]
        list_in.append(i)
        # print(list_in)
        # print(text_match(patterns[0],list_in[0][0]))
        if list_in[0][0]==type[0]:
                name=list_in[0][1]  ###get name of module
        elif list_in[0][0]==type[1]:
                # print(list_in[0][0])
                if text_match(patterns[4],list_in[0][1]): ##if there is a match
                        invabus=list_in[0][1]
                        n=invabus.split(',')
                        n1=n[0].split(' ')
                        inputs.append(n1[1])           ###abb a input with bus
                        size_inputs.append(n1[0])      ##abb the size of a input 
                        for i in range(1,len(n)):
                                inputs.append(n[i])
                                size_inputs.append(n1[0])
                else:
                        inva=list_in[0][1]                  ##get inputs without bus
                        n=inva.split(',')
                        for i in range(0,len(n)):
                                inputs.append(n[i])
                                size_inputs.append('[0,0]')
        elif list_in[0][0]==type[2]:
                if text_match(patterns[4],list_in[0][1]): ##if there is a match
                        invabus=list_in[0][1]
                        n=invabus.split(',')
                        n1=n[0].split(' ')
                        outputs.append(n1[1])           ###abb a input with bus
                        size_outputs.append(n1[0])      ##abb the size of a input 
                        for i in range(1,len(n)):
                                outputs.append(n[i])
                                size_outputs.append(n1[0])
                else:
                        inva=list_in[0][1]                  ##get inputs without bus
                        n=inva.split(',')
                        for i in range(0,len(n)):
                                outputs.append(n[i])
                                size_outputs.append('[0,0]')
        
######****************************Get information of states table*********************************
    big_list_state=[]
    big_list_output=[]
    list_state=[]
    posi=0
    for j in range(0,len(edopp)):
        small_list_state=[]
        small_list_output=[]
        list_state.append(edopp[j][0])
        for i in range(0,ncomb):
                small_list_state.append(edofp[posi+i][0])
                small_list_output.append(state_outputp[posi+i])
        if(i==1):
         posi=posi+2               
        big_list_state.append(small_list_state)
        big_list_output.append(small_list_output)
        

    module=dict(name=entityinf[0][1])
    inputports={'name':inputs,'size':size_inputs}
    outputports={'name':outputs,'size':size_outputs}
    states={'presentes_states':list_state,'futures_states':big_list_state,'output':big_list_output}

    return  module, inputports,outputports, states