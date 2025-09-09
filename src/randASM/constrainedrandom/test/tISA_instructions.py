import vsc
from randASM.constrainedrandom.base_classes.cl_cr_instruction import cl_instruction
from randASM.constrainedrandom.base_classes.cl_cr_operands import cl_immediate
from randASM.constrainedrandom.base_classes.cl_cr_registers import cl_register
from randASM.constrainedrandom.test.tISA_registers import tISA_register_bank

class instr_add(cl_instruction):
    def __init__(self):
        super().__init__("add")
        self.operands = {
            "rd": cl_register(reg_bank=tISA_register_bank),
            "rs1": cl_register(reg_bank=tISA_register_bank),
            "rs2": cl_register(reg_bank=tISA_register_bank)
        }

class instr_addi(cl_instruction):
    def __init__(self):
        super().__init__("addi")
        self.operands = {
            "rd": cl_register(reg_bank=tISA_register_bank),
            "imm": cl_immediate(8)
        }

class instr_slli(cl_instruction):
    def __init__(self):
        super().__init__("slli")
        self.operands = {
            "rd": cl_register(reg_bank=tISA_register_bank),
            "rs1": cl_register(reg_bank=tISA_register_bank),
            "imm": cl_immediate(4)
        }

class instr_srli(cl_instruction):
    def __init__(self):
        super().__init__("srli")
        self.operands = {
            "rd": cl_register(reg_bank=tISA_register_bank),
            "rs1": cl_register(reg_bank=tISA_register_bank),
            "imm": cl_immediate(4)
        }

class instr_lui(cl_instruction):
    def __init__(self):
        super().__init__("lui")
        self.operands = {
            "rd": cl_register(reg_bank=tISA_register_bank),
            "imm": cl_immediate(8)
        }

class instr_li(cl_instruction):
    def __init__(self):
        super().__init__("li")
        self.operands = {
            "rd": cl_register(reg_bank=tISA_register_bank),
            "imm": cl_immediate(16)
        }

class instr_jal(cl_instruction):
    def __init__(self):
        super().__init__("jal")
        self.operands = {
            "rd": cl_register(reg_bank=tISA_register_bank),
            "label": cl_label_op()
        }

class instr_beq(cl_instruction):
    def __init__(self):
        super().__init__("beq")
        self.operands = {
            "rd": cl_register(reg_bank=tISA_register_bank),
            "rs1": cl_register(reg_bank=tISA_register_bank),
            "label": cl_label_op()
        }

class instr_l(cl_instruction):
    def __init__(self):
        super().__init__("l")
        self.operands = {
            "rd": cl_register(reg_bank=tISA_register_bank),
            "rs1": cl_register(reg_bank=tISA_register_bank),
            "imm": cl_immediate()
        }

class instr_s(cl_instruction):
    def __init__(self):
        super().__init__("s")
        self.operands = {
            "rs1": cl_register(reg_bank=tISA_register_bank),
            "rs2": cl_register(reg_bank=tISA_register_bank),
            "imm": cl_immediate()
        }
