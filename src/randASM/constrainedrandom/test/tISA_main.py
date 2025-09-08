from constrainedrandom import *
from randASM.constrainedrandom.base_classes.cl_cr_instruction import cl_instruction_bank
from randASM.constrainedrandom.test.tISA_instructions import *

if __name__ == "__main__":
    tISA_instr_list = cl_instruction_bank()
    tISA_instr_list.register_instruction(add=instr_add,
                                         addi=instr_addi,
                                         slli=instr_slli,
                                         srli=instr_srli,
                                         lui=instr_lui,
                                         li=instr_li)
                                         # jal=instr_jal,
                                         # beq=instr_beq,
                                         # l=instr_l,
                                         # s=instr_s)
    program = RandObj()
    program.add_rand_var('instruction_list',domain=tISA_instr_list._instr_dict.keys(),length=100)
    program.randomize()

    instructions = []
    for instr_mn in program.instruction_list:
        instructions.append(tISA_instr_list.get_instruction(instr_mn))
        instructions[-1].randomize()

    for instr in instructions:
        print(instr.get_asm_str())

