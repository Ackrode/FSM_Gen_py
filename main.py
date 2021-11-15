from get_info import *

table='state_table.txt'
module, inputs, outputs, states = get_info(table)
# get_info(table)
print(module)
print(inputs)
print(outputs)
print(states)