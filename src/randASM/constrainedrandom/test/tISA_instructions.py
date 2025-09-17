import vsc
from randASM.constrainedrandom.base_classes.cl_instruction import cl_instruction
from randASM.constrainedrandom.base_classes.cl_registers import cl_register
from randASM.constrainedrandom.base_classes.cl_immediates import cl_immediate_bank
from randASM.constrainedrandom.test.tISA_registers import tISA_register_bank

imm_8_bit = cl_immediate_bank(size=8)
imm_4_bit = cl_immediate_bank(size=4)
imm_16_bit = cl_immediate_bank(size=16)

class instr_add(cl_instruction):
    def __init__(self):
        super().__init__(
            mnemonic="add",
            rd=tISA_register_bank,
            rs1=tISA_register_bank,
            rs2=tISA_register_bank,
        )

class instr_addi(cl_instruction):
    def __init__(self):
        super().__init__(
            mnemonic="addi",
            rd=tISA_register_bank,
            im=imm_8_bit
        )

class instr_slli(cl_instruction):
    def __init__(self):
        super().__init__(
            mnemonic="slli",
            rd=tISA_register_bank,
            rs1=tISA_register_bank,
            imm=imm_4_bit
        )

class instr_srli(cl_instruction):
    def __init__(self):
        super().__init__(
            mnemonic="srli",
            rd=tISA_register_bank,
            rs1=tISA_register_bank,
            imm=imm_4_bit
        )

class instr_lui(cl_instruction):
    def __init__(self):
        super().__init__(
            mnemonic="lui",
            rd=tISA_register_bank,
            imm=imm_8_bit
        )

class instr_li(cl_instruction):
    def __init__(self):
        super().__init__(
            mnemonic="li",
            rd=tISA_register_bank,
            imm=imm_16_bit
        )

# class instr_jal(cl_instruction):
#     def __init__(self):
#         super().__init__("jal")
#         self.operands = {
#             "rd": tISA_register_bank,
#             "label": cl_label_op()
#         )
#
# class instr_beq(cl_instruction):
#     def __init__(self):
#         super().__init__("beq")
#         self.operands = {
#             "rd": tISA_register_bank,
#             "rs1": tISA_register_bank,
#             "label": cl_label_op()
#         )
#
# class instr_l(cl_instruction):
#     def __init__(self):
#         super().__init__("l")
#         self.operands = {
#             rd=tISA_register_bank,
#             rs1=tISA_register_bank,
#             imm=cl_immediate()
#         )
#
# class instr_s(cl_instruction):
#     def __init__(self):
#         super().__init__("s")
#         self.operands = {
#             rs1=tISA_register_bank,
#             rs2=tISA_register_bank,
#             imm=cl_immediate()
#         )
