import vsc
from randASM.constrainedrandom.base_classes.cl_cr_instruction import cl_instruction
from randASM.constrainedrandom.base_classes.cl_cr_operands import cl_immediate
from randASM.constrainedrandom.base_classes.cl_cr_registers import cl_register
from randASM.constrainedrandom.test.tISA_registers import tISA_register_bank

class instr_add(cl_instruction):
    def __init__(self):
        super().__init__("add")
        self.operands = {
            "rd ": cl_register(reg_bank=tISA_register_bank),
            "rs1 ": cl_register(reg_bank=tISA_register_bank),
            "rs2 ": cl_register(reg_bank=tISA_register_bank)
        }

    # def get_asm_str(self):
    #     return "add {}, {}, {}".format(
    #        self.rd.get_asm_str(),
    #        self.rs1.get_asm_str(),
    #        self.rs2.get_asm_str()
    #    )
    #
class instr_addi(cl_instruction):
    def __init__(self):
        super().__init__("addi")
        self.operands = {
            "rd ": cl_register(reg_bank=tISA_register_bank),
            "imm ": cl_immediate(8)
        }

    # def get_asm_str(self):
    #     return "addi {}, {}".format(
    #        self.rd.get_asm_str(),
    #        self.imm.get_asm_str()
    #     )

class instr_slli(cl_instruction):
    def __init__(self):
        super().__init__("slli")
        self.operands = {
            "rd ": cl_register(reg_bank=tISA_register_bank),
            "rs1 ": cl_register(reg_bank=tISA_register_bank),
            "imm ": cl_immediate(4)
        }

    # def get_asm_str(self):
    #     return "slli {},{},{}".format(
    #        self.rd.get_asm_str(),
    #        self.rs1.get_asm_str(),
    #        self.imm.get_asm_str()
    #     )


class instr_srli(cl_instruction):
    def __init__(self):
        super().__init__("srli")
        self.operands = {
            "rd ": cl_register(reg_bank=tISA_register_bank),
            "rs1 ": cl_register(reg_bank=tISA_register_bank),
            "imm ": cl_immediate(4)
        }

    # def get_asm_str(self):
    #     return "srli {}, {},{}".format(
    #        self.rd.get_asm_str(),
    #        self.rs1.get_asm_str(),
    #        self.imm.get_asm_str()
    #     )

class instr_lui(cl_instruction):
    def __init__(self):
        super().__init__("lui")
        self.operands = {
            "rd ": cl_register(reg_bank=tISA_register_bank),
            "imm ": cl_immediate(8)
        }

    # def get_asm_str(self):
    #     return "lui {}, {}".format(
    #        self.rd.get_asm_str(),
    #        self.imm.get_asm_str()
    #     )

class instr_li(cl_instruction):
    def __init__(self):
        super().__init__("li")
        self.operands = {
            "rd ": cl_register(reg_bank=tISA_register_bank),
            "imm ": cl_immediate(16)
        }

    # def get_asm_str(self):
    #     return "li {}, {}".format(
    #        self.rd.get_asm_str(),
    #        self.imm.get_asm_str()
    #     )

class instr_jal(cl_instruction):
    def __init__(self):
        super().__init__("jal")
        self.operands = {
            "rd ": cl_register(reg_bank=tISA_register_bank),
            "label ": cl_label_op()
        }

    # def get_asm_str(self):
    #     return "jal {}, {}".format(
    #        self.rd.get_asm_str(),
    #        self.label.get_asm_str()
    #     )

class instr_beq(cl_instruction):
    def __init__(self):
        super().__init__("beq")
        self.operands = {
            "rd ": cl_register(reg_bank=tISA_register_bank),
            "rs1 ": cl_register(reg_bank=tISA_register_bank),
            "label ": cl_label_op()
        }

    # def get_asm_str(self):
    #     return "beq {}, {}, {}".format(
    #        self.rd.get_asm_str(),
    #        self.rd.get_asm_str(),
    #        self.label.get_asm_str()
    #    )

class instr_l(cl_instruction):
    def __init__(self):
        super().__init__("l")
        self.operands = {
            "rd ": cl_register(reg_bank=tISA_register_bank),
            "rs1 ": cl_register(reg_bank=tISA_register_bank),
            "imm ": cl_immediate()
        }

    # def get_asm_str(self):
    #     return "l {}, {}, {}".format(
    #        self.rd.get_asm_str(),
    #        self.rs1.get_asm_str(),
    #        self.imm.get_asm_str()
    #     )


class instr_s(cl_instruction):
    def __init__(self):
        super().__init__("s")
        self.operands = {
            "rs1 ": cl_register(reg_bank=tISA_register_bank),
            "rs2 ": cl_register(reg_bank=tISA_register_bank),
            "imm ": cl_immediate()
        }

    # def get_asm_str(self):
    #     return "s {}, {}, {}".format(
    #        self.rs1.get_asm_str(),
    #        self.rs2.get_asm_str(),
    #        self.imm.get_asm_str()
    # )
