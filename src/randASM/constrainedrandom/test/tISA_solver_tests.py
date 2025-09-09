from constrainedrandom import *
from randASM.constrainedrandom.base_classes.cl_cr_instruction import cl_instruction_bank
from randASM.constrainedrandom.base_classes.cl_cr_instruction_sequence import cl_instruction_sequence
from randASM.constrainedrandom.test.tISA_instructions import *


if __name__ == "__main__":
    tISA_instr_bank = cl_instruction_bank()
    tISA_instr_bank.register_instruction(add=instr_add,
                                         addi=instr_addi,
                                         slli=instr_slli,
                                         srli=instr_srli,
                                         lui=instr_lui,
                                         li=instr_li)
                                         # jal=instr_jal,
                                         # beq=instr_beq,
                                         # l=instr_l,
                                         # s=instr_s)

    program = cl_instruction_sequence(instr_bank=tISA_instr_bank)

    def is_li(x):
        return x=="li"

    program.randomize()
    program.get_instructions()
    program.add_constraint(is_li,('mnemonic_list',))

    def is_t0(x):
        return x == 0

    def lt_part(x):
        return x == 0 #< 2**16*0.001

    def is_even(x):
        return x%2 == 0

    for instr in program.instruction_list:

        if instr.get_mnemonic() == "li":
            instr.add_constraint(
                    rd=(is_t0,('_reg_num',)),
                    imm=(lt_part,('_val',))
            )

    program.randomize_instructions()
    print(program.get_asm_str())
