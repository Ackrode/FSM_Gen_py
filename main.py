from get_info import get_info
from next_state import next_state
from Output_Logic import output_logic
from state import get_state
from backbone import backbone
from stimulus import stimulus
import copy
table='state_table.txt'
path='design.v'
module, inputs, outputs, states=get_info(table)
input=copy.deepcopy(inputs)
get_state(path, module, inputs, outputs, states)
next_state(path, input, states)
output_logic(path,inputs, outputs, states)

backbone(inputs, outputs,module=module.get('name'))
stimulus(module.get('name'), states)
# get_info(table)
