import vsc
from randASM.pyvsc.base_classes.cl_pyvsc_instruction import cl_instruction
from randASM.pyvsc.base_classes.cl_pyvsc_operands import cl_immediate
from randASM.pyvsc.base_classes.cl_pyvsc_registers import cl_register
from randASM.pyvsc.test.tISA_registers import tISA_register_bank

@vsc.randobj
class instr_add(cl_instruction):
    def __init__(self):
        super().__init__("add")
        self.rd = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.rs1 = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.rs2 = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))

    def get_asm_str(self):
        return "add {}, {}, {}".format(
           self.rd.get_asm_str(),
           self.rs1.get_asm_str(),
           self.rs2.get_asm_str()
       )

@vsc.randobj
class instr_addi(cl_instruction):
    def __init__(self):
        super().__init__("addi")
        self.rd = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.imm = vsc.rand_attr(cl_immediate(8))

    def get_asm_str(self):
        return "addi {}, {}".format(
           self.rd.get_asm_str(),
           self.imm.get_asm_str()
        )

@vsc.randobj
class instr_slli(cl_instruction):
    def __init__(self):
        super().__init__("slli")
        self.rd = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.rs1 = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.imm = cl_immediate(4)

    def get_asm_str(self):
        return "slli {},{},{}".format(
           self.rd.get_asm_str(),
           self.rs1.get_asm_str(),
           self.imm.get_asm_str()
        )


@vsc.randobj
class instr_srli(cl_instruction):
    def __init__(self):
        super().__init__("srli")
        self.rd = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.rs1 = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.imm = cl_immediate(4)

    def get_asm_str(self):
        return "srli {}, {},{}".format(
           self.rd.get_asm_str(),
           self.rs1.get_asm_str(),
           self.imm.get_asm_str()
        )

@vsc.randobj
class instr_lui(cl_instruction):
    def __init__(self):
        super().__init__("lui")
        self.rd = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.imm = vsc.rand_attr(cl_immediate(8))

    def get_asm_str(self):
        return "lui {}, {}".format(
           self.rd.get_asm_str(),
           self.imm.get_asm_str()
        )

@vsc.randobj
class instr_li(cl_instruction):
    def __init__(self):
        super().__init__("li")
        self.rd = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.imm = cl_immediate(16)

    def get_asm_str(self):
        return "li {}, {}".format(
           self.rd.get_asm_str(),
           self.imm.get_asm_str()
        )

@vsc.randobj
class instr_jal(cl_instruction):
    def __init__(self):
        super().__init__("jal")
        self.rd = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.label = cl_label_op()

    def get_asm_str(self):
        return "jal {}, {}".format(
           self.rd.get_asm_str(),
           self.label.get_asm_str()
        )

@vsc.randobj
class instr_beq(cl_instruction):
    def __init__(self):
        super().__init__("beq")
        self.rd = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.rs1 = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.label = cl_label_op()

    def get_asm_str(self):
        return "beq {}, {}, {}".format(
           self.rd.get_asm_str(),
           self.rd.get_asm_str(),
           self.label.get_asm_str()
       )

@vsc.randobj
class instr_l(cl_instruction):
    def __init__(self):
        super().__init__("l")
        self.rd = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.rs1 = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.imm = cl_immediate()

    def get_asm_str(self):
        return "l {}, {}, {}".format(
           self.rd.get_asm_str(),
           self.rs1.get_asm_str(),
           self.imm.get_asm_str()
        )

@vsc.randobj
class instr_s(cl_instruction):
    def __init__(self):
        super().__init__("s")
        self.rs1 = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.rs2 = vsc.rand_attr(cl_register(reg_bank=tISA_register_bank))
        self.imm = cl_immediate()

    def get_asm_str(self):
        return "s {}, {}, {}".format(
           self.rs1.get_asm_str(),
           self.rs2.get_asm_str(),
           self.imm.get_asm_str()
        )
