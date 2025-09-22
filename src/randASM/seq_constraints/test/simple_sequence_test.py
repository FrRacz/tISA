from randASM.seq_constraints.test.tISA_instructions import instruction_pool, instr_add
from randASM.seq_constraints.classes.cl_meta_instruction import cl_meta_instruction
from randASM.seq_constraints.classes.cl_instruction_sequence import cl_instruction_sequence

meta_arith = cl_meta_instruction(instruction_pool)
def is_arith(x):
    return x.instr_type == 'arith'

meta_arith.add_constraint(is_arith,('instr',))

meta_imm_gen = cl_meta_instruction(instruction_pool)

def is_imm_gen(x):
    return x.instr_type == 'imm_gen'

meta_imm_gen.add_constraint(is_imm_gen,('instr',))
meta_imm_gen.add_required_instr(instr_add,range(1,3))

imm_gen = cl_meta_instruction(instruction_pool)
imm_gen.add_constraint(is_imm_gen,('instr',))



seq = cl_instruction_sequence()
seq.append(imm_gen,meta_imm_gen,imm_gen)
seq.randomize()
print(seq.get_asm_str())
