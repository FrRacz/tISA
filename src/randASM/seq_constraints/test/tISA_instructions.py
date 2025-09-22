from randASM.seq_constraints.classes.cl_instructions import cl_instruction
from randASM.seq_constraints.classes.cl_instruction_pool import cl_instruction_pool
from randASM.seq_constraints.classes.cl_registers import cl_register
from randASM.seq_constraints.classes.cl_immediate_pool import cl_immediate_pool
from randASM.seq_constraints.test.tISA_registers import tISA_register_pool

imm_8_bit = cl_immediate_pool(size=8)
imm_4_bit = cl_immediate_pool(size=4)
imm_16_bit = cl_immediate_pool(size=16)

class instr_add(cl_instruction):
    instr_type = 'arith'
    def __init__(self):
        super().__init__(
            mnemonic="add",
            rd=tISA_register_pool,
            rs1=tISA_register_pool,
            rs2=tISA_register_pool,
        )

class instr_addi(cl_instruction):
    instr_type = 'arith'
    def __init__(self):
        super().__init__(
            mnemonic="addi",
            rd=tISA_register_pool,
            im=imm_8_bit
        )

class instr_slli(cl_instruction):
    instr_type = 'arith'
    def __init__(self):
        super().__init__(
            mnemonic="slli",
            rd=tISA_register_pool,
            rs1=tISA_register_pool,
            imm=imm_4_bit
        )

class instr_srli(cl_instruction):
    instr_type = 'arith'
    def __init__(self):
        super().__init__(
            mnemonic="srli",
            rd=tISA_register_pool,
            rs1=tISA_register_pool,
            imm=imm_4_bit
        )

class instr_lui(cl_instruction):
    instr_type = 'imm_gen'
    def __init__(self):
        super().__init__(
            mnemonic="lui",
            rd=tISA_register_pool,
            imm=imm_8_bit
        )

class instr_li(cl_instruction):
    instr_type = 'imm_gen'
    def __init__(self):
        super().__init__(
            mnemonic="li",
            rd=tISA_register_pool,
            imm=imm_16_bit
        )

instruction_pool = cl_instruction_pool()
instruction_pool.register_instruction(
        add=instr_add,
        addi=instr_addi,
        slli=instr_slli,
        srli=instr_srli,
        lui=instr_lui,
        li=instr_li
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
