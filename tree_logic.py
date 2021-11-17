from get_info import *
module, inputports,outputports, states=get_info('state_table.txt')
j=0
for i in states.get('presentes_states'):
    for k in range(len(states.get('futures_states')[j])):
        print(states.get('futures_states')[j][k])
    j+=1