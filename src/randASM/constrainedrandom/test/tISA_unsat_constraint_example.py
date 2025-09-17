from constrainedrandom import *
from randASM.constrainedrandom.base_classes.cl_instruction import cl_instruction_bank
from randASM.constrainedrandom.base_classes.cl_instruction_sequence import cl_instruction_sequence
from randASM.constrainedrandom.test.tISA_instructions import *


if __name__ == "__main__":
    tISA_instr_bank = cl_instruction_bank()
    tISA_instr_bank.register_instruction(add=instr_addi_only_even,
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

    # Example of unsatisfiable constraint
    def first_10_add(x):
        return x[:10] == ["add"] * 10

    program.add_constraint(first_10_add,('mnemonic_list',))
    program.randomize()
    program.get_instructions()
    program.randomize_instructions()
    print(program.get_asm_str())


    def is_t0(x):
        return x == 0

    for instr in instructions:
        if instr.get_mnemonic() == "add":
            instr.operands["rd"].add_constraint(is_t0,('_reg_num',))

    for instr in instructions:
        instr.randomize()

    for instr in instructions:
        print(instr.get_asm_str())

