import random
import vsc
from enum import Enum

def create_asm_str(mnemonic:str,operands:dict):
        asm_str = f"{mnemonic} "
        for op in operands.values():
            asm_str += f"{op.get_asm_str()}, "
        asm_str = asm_str[:-2] # delete last space and comma
        return asm_str

def extend_enum(enum_cls, name, value):
    members = {m.name: m.value for m in enum_cls}
    members[name] = value
    return Enum(enum_cls.__name__, members)

@vsc.randobj
class cl_instruction_bank():
    def __init__(self,*args):
        self._instr_dict = {}
        self._instr_enum = Enum()
        # populate the instruction dictornary
        for i,instr in enumerate(args):
            self._instr_dict[i] = instr #careful this is just a rererence
            self._instr_enum = extend_enum(self._instr_enum,instr.__name__, i)
        self._valid_list = vsc.list_t(vsc.int_t(),len(self._instr_dict))

    def get_rand_intruction(self):
        instr = random.choice(list(self._instr_dict.values()))

        return instr()



@vsc.randobj
class cl_instruction():
    def __init__(self,mnemonic:str,operands:dict):
        self._name = mnemonic
        self.mnemonic = mnemonic
        self.operands = operands
        self.asm_str = create_asm_str(self.mnemonic,self.operands)


    def get_asm_str(self):
        return self.asm_str

    def get_name(self):
        return self._name

