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

    program.randomize()
    program.get_instructions()

    def is_t0(x):
        return x == 0

    def lt_five(x):
        return x < 2**16*0.05

    def is_even(x):
        return x%2 == 0

    for instr in program.instruction_list:
        if instr.get_mnemonic() == "add":
            instr.add_constraint(rd=(is_t0,('_reg_num',)))

        if instr.get_mnemonic() == "li":
            instr.add_constraint(
                    rd=(is_t0,('_reg_num',)),
                    imm=(lt_five,('_val',))
            )

    program.randomize_instructions()
    print(program.get_asm_str())

    for instr in program.instruction_list:
        if instr.get_mnemonic() == "li":
            instr.remove_constraint('rd')
    program.randomize_instructions()

    print('-'*10)
    print(program.get_asm_str())
