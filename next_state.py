from get_info import get_info
def get_n(inputs=[]):
    n=0


    if inputs:
# Iterate through the inputs
        for i in inputs.get('size'):
            N1=int(i[1])
            N2=int(i[3])
            print(N1,N2)
            n=n+abs(N1-N2)+1
 

    return n
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
with open('design.sv','w', encoding='utf-8') as f:    
    design=['']
    table='state_table.txt'
    module, inputs, outputs, states=get_info(table)
    #delete first 2 keys of inputs.get('name') dictionary
    del inputs.get('name')[0]
    del inputs.get('size')[0]
    del inputs.get('name')[0]
    del inputs.get('size')[0]
    print(inputs)
    n=get_n(inputs)
    print(n)
    design.append('always @(state ,'+convert(inputs.get('name'))+')')
    design.append('\tbegin')
    design.append('\t\tcase(state)')
    i=0
    for current_state in states.get('presentes_states'):
        design.append('\t\t\t'+current_state+':')
        design.append('\t\t\t\tbegin')
        for j in range(0,n+1):
            design.append ('\t\t\t\t\tif('+convert(inputs.get('name'))+'=='+str(j)+')')
            design.append('\t\t\t\t\t\tnext_state<='+states.get('futures_states')[i][j]+';')
        design.append('\t\t\t\tend')
        i+=1
    design.append('\t\tendcase')
    design.append('\tend')
    #print(design)
    for line in design:
        f.write(line+'\n')
    f.close()
