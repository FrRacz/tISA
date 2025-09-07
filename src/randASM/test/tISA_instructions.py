from randASM.pyvsc_base_classes.cl_pyvsc_instruction import *
from randASM.pyvsc_base_classes.cl_pyvsc_operands import *
from randASM.pyvsc_base_classes.cl_pyvsc_registers import *

class instr_add(cl_instruction):
    def __init__(self):
        super().__init__("add")
        self.rd = cl_register_op()
        self.rs1 = cl_register_op()
        self.rs2 = cl_register_op()

    def get_asm_str(self):
        return "add {}, {}, {}".format(
           self.rd.get_asm_str(),
           self.rs1.get_asm_str(),
           self.rs2.get_asm_str()
       )

class instr_addi(cl_instruction):
    def __init__(self):
        super().__init__("addi")
        self.rd = cl_register_op()
        self.imm = cl_immediate_op()

    def get_asm_str(self):
        return "addi {}, {}".format(
           self.rd.get_asm_str(),
           self.imm.get_asm_str()
        )

class instr_slli(cl_instruction):
    def __init__(self):
        super().__init__("slli")
        self.rd = cl_register_op()
        self.rs1 = cl_register_op()
        self.imm = cl_immediate_op()

    def get_asm_str(self):
        return "slli {},{},{}".format(
               self.rd.get_asm_str(),
               self.rs1.get_asm_str(),
               self.imm.get_asm_str()
        )

class instr_srli(cl_instruction):
    def __init__(self):
        super().__init__("srli")
        self.rd = cl_register_op()
        self.rs1 = cl_register_op()
        self.imm = cl_immediate_op()

    def get_asm_str(self):
        return "srli {}, {},{}".format(
           self.rd.get_asm_str(),
           self.rs1.get_asm_str(),
           self.imm.get_asm_str()
        )

class instr_lui(cl_instruction):
    def __init__(self):
        super().__init__("lui")
        self.rd = cl_register_op()
        self.imm = cl_immediate_op()

    def get_asm_str(self):
        return "lui {}, {}".format(
           self.rd.get_asm_str(),
           self.imm.get_asm_str()
        )


class instr_li(cl_instruction):
    def __init__(self):
        super().__init__("li")
        self.rd = cl_register_op()
        self.imm = cl_immediate_op()

    def get_asm_str(self):
        return "li {}, {}".format(
           self.rd.get_asm_str(),
           self.imm.get_asm_str()
        )

class instr_jal(cl_instruction):
    def __init__(self):
        super().__init__("jal")
        self.rd = cl_register_op()
        self.label = cl_label_op()

    def get_asm_str(self):
        return "jal {}, {}".format(
           self.rd.get_asm_str(),
           self.label.get_asm_str()
        )

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
        return "l {}, {}, {}".format(
           self.rd.get_asm_str(),
           self.rs1.get_asm_str(),
           self.imm.get_asm_str()
        )


class instr_s(cl_instruction):
    def __init__(self):
        super().__init__("s")
        self.rs1 = cl_register_op()
        self.rs2 = cl_register_op()
        self.imm = cl_immediate_op()

    def get_asm_str(self):
        return "s {}, {}, {}".format(
           self.rs1.get_asm_str(),
           self.rs2.get_asm_str(),
           self.imm.get_asm_str()
        )
