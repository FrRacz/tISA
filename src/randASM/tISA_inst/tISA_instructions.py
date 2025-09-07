from randASM.base_classes.cl_instruction import cl_instruction,cl_instruction_list
from randASM.base_classes.cl_operands import *


class instr_add(cl_instruction):
    def __init__(self):
        super().__init__("add")
        self.rd = cl_register_op()
        self.rs1 = cl_register_op()
        self.rs2 = cl_register_op()

    def get_asm_str(self):
        return "add " + \
               self.rd.get_asm_str() + ', ' +\
               self.rs1.get_asm_str() + ', ' +\
               self.rs2.get_asm_str()

class instr_addi(cl_instruction):
    def __init__(self):
        super().__init__("addi")
        self.rd = cl_register_op()
        self.imm = cl_immediate_op()

    def get_asm_str(self):
        return "addi " + \
               self.rd.get_asm_str() + ', ' +\
               self.imm.get_asm_str()

class instr_slli(cl_instruction):
    def __init__(self):
        super().__init__("slli")
        self.rd = cl_register_op()
        self.rs1 = cl_register_op()
        self.imm = cl_immediate_op()

    def get_asm_str(self):
        return "slli " + \
               self.rd.get_asm_str() + ', ' +\
               self.rs1.get_asm_str  + ', ' +\
               self.imm.get_asm_str()

class instr_srli(cl_instruction):
    def __init__(self):
        super().__init__("srli")
        self.rd = cl_register_op()
        self.rs1 = cl_register_op()
        self.imm = cl_immediate_op()

    def get_asm_str(self):
        return "srli " + \
               self.rd.get_asm_str() + ', ' +\
               self.rs1.get_asm_str  + ', ' +\
               self.imm.get_asm_str()

class instr_lui(cl_instruction):
    def __init__(self):
        super().__init__("lui")
        self.rd = cl_register_op()
        self.imm = cl_immediate_op()

    def get_asm_str(self):
        return "lui " + \
               self.rd.get_asm_str() + ', ' +\
               self.imm.get_asm_str()

class instr_li(cl_instruction):
    def __init__(self):
        super().__init__("li")
        self.rd = cl_register_op()
        self.imm = cl_immediate_op()

    def get_asm_str(self):
        return "li " + \
               self.rd.get_asm_str() + ', ' +\
               self.imm.get_asm_str()

class instr_jal(cl_instruction):
    def __init__(self):
        super().__init__("jal")
        self.rd = cl_register_op()
        self.label = cl_label_op()

    def get_asm_str(self):
        return "jal " +\
               self.rd.get_asm_str() + ', ' +\
               self.label.get_asm_str()

class instr_beq(cl_instruction):
    def __init__(self):
        super().__init__("beq")
        self.rd = cl_register_op()
        self.rs1 = cl_register_op()
        self.label = cl_label_op()

    def get_asm_str(self):
        return "beq " +\
               self.rd.get_asm_str() + ', ' +\
               self.rd.get_asm_str() + ', ' +\
               self.label.get_asm_str()

class instr_l(cl_instruction):
    def __init__(self):
        super().__init__("l")
        self.rd = cl_register_op()
        self.rs1 = cl_register_op()
        self.imm = cl_immediate_op()

    def get_asm_str(self):
        return "l " + \
               self.rd.get_asm_str() + ', ' +\
               self.rs1.get_asm_str  + ', ' +\
               self.imm.get_asm_str()

class instr_s(cl_instruction):
    def __init__(self):
        super().__init__("s")
        self.rs1 = cl_register_op()
        self.rs2 = cl_register_op()
        self.imm = cl_immediate_op()

    def get_asm_str(self):
        return "s " + \
               self.rs1.get_asm_str() + ', ' +\
               self.rs2.get_asm_str  + ', ' +\
               self.imm.get_asm_str()
