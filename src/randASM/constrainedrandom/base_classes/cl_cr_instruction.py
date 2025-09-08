from randASM.constrainedrandom.base_classes.cl_cr_registers import cl_register
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

class cl_instruction_bank():
    def __init__(self):
        self._instr_dict = {}

    def register_instruction(self, **instructions):
        for mnemonic, instr_cls in instructions.items():
            self._instr_dict[mnemonic] = instr_cls

    def get_instruction(self,mnemonic):
        instr = self._instr_dict[mnemonic]()
        return instr


class cl_instruction():
    def __init__(self,mnemonic):
        self._mnemonic = mnemonic
        self.operands = None

    def get_asm_str(self):
        return create_asm_str(self._mnemonic,self.operands)

    def randomize(self):
        for op in self.operands.values():
            op.randomize()


if __name__ == "__main__":
    class instr_add(cl_instruction):
        def __init__(self):
            super().__init__("add")

    class instr_addi(cl_instruction):
        def __init__(self):
            super().__init__("addi")

    instr_bank = cl_instruction_bank()
    instr_bank.register_instruction(
        add=instr_add,
        addi=instr_addi
            )

    instr = instr_bank.get_instruction("add")
    print(instr._mnemonic)
