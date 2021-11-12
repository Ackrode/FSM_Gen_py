design=['']
states={'A':['A', 'B']}
design.append('always @(state ,'+input.get('name')+')')
design.append('\tbegin')
design.append('\t\tcase(state)')
for current_state in states.keys():
    design.append('\t\t\t'+current_state+':')
    design.append('\t\t\t\tbegin')
    design.append('\t\t\t\t\tstate<='+states[i][1]+';')
    design.append('\t\t\t\tend')
