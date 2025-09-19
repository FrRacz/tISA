from z3.z3 import Solver,Int,sat,Distinct,Bool
from enum import Enum,auto

class sign(Enum):
    POSITIVE = auto()
    NEGATIVE = auto()

class Item():
    def __init__(self,name):
        self._name = name
        self._required = []

    def add_required(self,item,min_offset:int,max_offset:int,sign:sign):
        self._required.append({
            'item':item,
            'min_offset':min_offset,
            'max_offset':max_offset,
            'sign':sign
            })

    def get_name(self):
        return self._name

unsorted_list = []
for i in range(10):
    item = Item(f'I{i}')
    unsorted_list.append(item)
req_1 = Item(f"R1")
req_2 = Item(f"R2")
req_3 = Item(f"R3")

unsorted_list[4].add_required(req_1,2,2,sign.NEGATIVE)
unsorted_list[3].add_required(req_2,1,1,sign.POSITIVE)

s = Solver()
s_vars = {obj.get_name() : Int(obj.get_name()) for obj in unsorted_list}
s_vars_tracker = {}

for idx,item in enumerate(unsorted_list):
    item_var = s_vars[unsorted_list[idx].get_name()]
    if idx == len(unsorted_list) - 1:
        pass
    else:
        next_item_var = s_vars[unsorted_list[idx + 1].get_name()]
        tracker = Bool(f'{item.get_name()} seq_order')
        s_vars_tracker[f'{item.get_name()} seq_order'] = tracker
        s.assert_and_track(item_var < next_item_var,tracker)
    for r_item in item._required:
        s_vars[r_item['item'].get_name()] = Int(r_item['item'].get_name())
        r_item_var = s_vars[r_item['item'].get_name()]
        r_item_name = r_item['item'].get_name()
        min_offset_tracker = Bool(f"{r_item_name} min offset from {item.get_name()}")
        max_offset_tracker = Bool(f"{r_item_name} max offset from {item.get_name()}")
        s_vars_tracker[f"{r_item_name} min offset from {item.get_name()}"] = min_offset_tracker
        s_vars_tracker[f"{r_item_name} max offset from {item.get_name()}"] = max_offset_tracker
        if r_item['sign'] == sign.POSITIVE:
            s.assert_and_track(r_item_var >= item_var + r_item['min_offset'],min_offset_tracker)
            s.assert_and_track(r_item_var <= item_var + r_item['max_offset'],max_offset_tracker)
        elif r_item['sign'] == sign.NEGATIVE:
            s.assert_and_track(r_item_var <= item_var - r_item['max_offset'],min_offset_tracker)
            s.assert_and_track(r_item_var >= item_var - r_item['max_offset'],max_offset_tracker)
# Ensure solution is a permutation of indices in range(0,instr_count)

s.add(Distinct(*s_vars.values()))
N = len(s_vars)
for var in s_vars.values():
    s.add(var>=0,var<N)

if s.check() == sat:
    model = s.model()
    for name, var in s_vars.items():
        print(f"{name} = {model[var]}")
else:
    print("Failed to solve")
    print("Unsat core:", s.unsat_core())
    print('-'*10)
    print(s.to_smt2())
