from constrainedrandom import RandObj
import random
import randASM.seq_constraints.classes.cl_instruction_sequence as instr_seq

class cl_meta_instruction(RandObj):
    def __init__(self,instr_pool):
        super().__init__()
        self.add_rand_var('instr',domain=instr_pool.get_domain())
        self._instr_pool = instr_pool
        self.parent_sequence = None
        self._required = []

    def register_in_seq(self,parent_sequence:instr_seq.cl_instruction_sequence):
        self.parent_sequence = parent_sequence

    def add_required_instr(self,instr,location:range):
        self._required.append((instr,location))


    def resolve_required(self):
        for instr, location in self._required:
            idx = self.parent_sequence._instr_stream.index(self)
            offset = random.choice(location)

            self.parent_sequence._instr_stream.insert(idx+offset,instr())
            print(f"{self} at idx {idx}, inserting {instr}, at idx {idx+offset}")

    def randomize(self):
        super().randomize()
        return self.instr().randomize()
