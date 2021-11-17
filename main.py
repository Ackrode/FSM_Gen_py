from get_info import get_info
from next_state import next_state
from Output_Logic import output_logic
from state import get_state
table='state_table.txt'
path='design.v'
module, inputs, outputs, states=get_info(table)
print(inputs)
get_state(path, module, inputs, outputs, states)
next_state(path, inputs, states)
print(inputs)
output_logic(path,inputs, outputs, states)

# get_info(table)
