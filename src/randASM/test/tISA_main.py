from randASM.base_classes.cl_instruction import cl_instruction_bank
from randASM.tISA_inst.tISA_instructions import *

tISA_instr_list = cl_instruction_bank(instr_add,
                                      instr_addi,
                                      instr_slli,
                                      instr_srli,
                                      instr_lui,
                                      instr_li,
                                      instr_jal,
                                      instr_beq,
                                      instr_l,
                                      instr_s)
for _ in range(100):
    instr = tISA_instr_list.get_rand_intruction()
    print(instr.get_name())
