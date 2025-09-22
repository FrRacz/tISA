class cl_instruction_pool():
    """
    Class to hold all instructions of a ISA.
    """
    def __init__(self):
        self._instr_dict = {}

    def register_instruction(self, **instructions):
        """
        Add a new instruction to the instruction dictionary
        """
        for mnemonic, instr_cls in instructions.items():
            self._instr_dict[mnemonic] = instr_cls

    def get_domain(self):
        return self._instr_dict.values()
