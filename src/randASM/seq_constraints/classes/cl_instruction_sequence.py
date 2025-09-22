import randASM.seq_constraints.classes.cl_meta_instruction as meta_instr

class cl_instruction_sequence():
    def __init__(self):
        self._instr_stream = []
        self._asm_stream = []

    def append(self,*elements):
        for elem in elements:
            if isinstance(elem,meta_instr.cl_meta_instruction):
                elem.register_in_seq(self)
                self._instr_stream.append(elem)

    def randomize(self):
        # resolve meta-instr requiremments
        for instr in self._instr_stream:
            if isinstance(instr,meta_instr.cl_meta_instruction):
                instr.resolve_required()

        for instr in self._instr_stream:
            print(instr)
            randomized_instr = instr.randomize()
            self._asm_stream.append(randomized_instr)

    def get_asm_str(self):
        asm = ""
        for instr in self._asm_stream:
            asm += instr.get_asm_str()
        return asm
